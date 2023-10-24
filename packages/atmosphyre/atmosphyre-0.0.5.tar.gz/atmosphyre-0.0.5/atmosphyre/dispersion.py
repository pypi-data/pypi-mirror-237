import numpy as np
import matplotlib.pyplot as plt
from atmosphyre import dispersion_functions as diff_func
import matplotlib as mpl

class sim:
    """This is the class for the module's atmospheric dispersion simulations.
    
    :param telescope_diameter: Telescope diameter, in metres. Default = 39m.
    :type telescope_diameter: float
    :param wavefront_outer_scale: Characteristic wavefront outer scale. Default = 46m.
    :type wavefront_outer_scale: float
    :param seeing: Seeing for the observation, in arcsec. Default = 0.68 arcsec.
    :type seeing: float
    :param seeing_wl: Wavelength of the given seeing measurement for the observation, in micrometers. Default = 0.5um.
    :type seeing_wl: float
    :param simulation_scale: Pixel scale of the simulation, in arcsec/pixel. Default = 0.01 arcsec/pixel, which shows high accuracy.
    :type simulation_scale: float
    :param simulation_intervals: Number of intervals in the observation to simulate for and calculate transmission. Default = 21.
    :type simulation_intervals: int
    :param latitude: Latitude of the telescope, in degrees. Default = -24.63 degrees.
    :type latitude: float
    :param temperature: Environment temperature at the telescope, in degrees celsius. Default = 10 degC.
    :type temperature: float
    :param humidity: Environment relative humidity at the telescope, in %. Default = 14.5%
    :type humidity: float
    :param pressure: Environment pressure at the telescope, in mBa. Default = 750mBa.
    :type pressure: float
    :param centring: The time of the observation at which the position of the apertures is determined by. Either 0.5 for halfway (default), or if an integer this will be the index of the simulation intervals.
    :type centring: float
    :param relative_plate_PA_angle: Relative angle of the apertures/focal plate and the North Celestial Pole direction, in degrees. For the aperture semi-major axis to be pointed along the NCP direction, set to 90 degrees. Default = 0 degrees.
    :type relative_plate_PA_angle: float

    To create the target class and run functions::
    
        from atmosphyre import dispersion

        simulation = dispersion.sim(**kwargs)
        simulation.chosen_function(parameters=parameter_values)

    """
    def __init__(self,**kwargs):
        """
        Instance Initializer - see class documentation for parameters.
        """
        self.input={}
        self.output={}
        
        self.config={
        'telescope_diameter':39, #m
        'wavefront_outer_scale':46, #m
        'seeing':.68, #arcsec
        'seeing_wl':.5, #um
        'simulation_scale':0.01, #arcsec/pixel, default is 0.01
        'simulation_intervals':21, #number of intervals in the HA range to simulate
        'relative_plate_PA_angle':0, #deg, relative angle of the plate/apertures and PA=0. For PA=0 along aperture semi major axis, set to 90 deg
        'centring':0.5, #either 0.5 for mid index, or HA index
        'latitude':-24.6272, #deg
        'temperature':10, #deg C
        'humidity':14.5, #%
        'pressure':750.0 #mBa
        }
        
        self.config.update(kwargs)
        
        #note: for a slit spectrograph, this relative_plate_PA_angle becomes vital. will need to implement a slit aperture using "width" and "height",
        #and implement 
        
    def load_wavelengths(self,wavelengths=[]):
        """
        Input the desired wavelengths for the analysis. Shifts and transmissions will be calculated for these.

        :param wavelengths: Wavelengths to calculate transmission for, units of micrometers (um).
        :type wavelengths: list of float
        """
        self.output['wavelengths']=np.array(wavelengths)

    def load_observation(self,observation_start=0,observation_end=1,declination=-30):
        """
        Input the observation/target details. This calculates the airmasses and parallatic angles for the observation.
        
        :param observation_start: Start of the observation in terms of hour angles, default = 0h.
        :type observation_start: float
        :param observation_end: End of the observation in terms of hour angles, default = 1h.
        :type observation_end: float
        :param declination: Declination of the observation target, in degrees. Default = -30 deg.
        :type declination: float
        """
        HA_range=np.linspace(observation_start,observation_end,self.config['simulation_intervals'])
        self.input['HA_range']=HA_range
        self.input['declination']=declination

        #latitude needs to be negative for now
        lat = float(self.config['latitude']) * np.pi/180
        dec = declination*np.pi/180
        
        #Need to check if the target is below the horizon for the given list of HA, and if so remove it.
        LHA_below_horizon=np.rad2deg(np.arccos(-np.tan(lat)*np.tan(dec)))/15 
        if str(LHA_below_horizon) != 'nan': 
            #print("Target goes below Horizon above/below HA of +/- %2.1fh" % (LHA_below_horizon))
            for val in HA_range.copy(): 
                if abs(val) > abs(LHA_below_horizon):
                    print("At HA %2.2fh, target goes below horizon - removing this from HA range" % (val))
                    HA_range.remove(val)        
        if dec > np.pi/2 + lat: #If the target has a too high declination, it will never be seen at Cerro Paranal
            print("Target always below Horizon")
            return

        airmasses=1/(np.sin(lat)*np.sin(dec)+np.cos(lat)*np.cos(dec)*np.cos(np.array(HA_range)*2*np.pi/24))
        self.output['airmasses']=np.array(airmasses)

        self.input['ZA_range']=diff_func.airmass_to_ZA(airmasses)
        
        para_angles=diff_func.parallatic_angle(np.array(HA_range),dec,lat)
        self.output['raw_para_angles']=np.array(para_angles) #actual PAs    
        
    def calculate_integration_shifts(self, guide_wavelength=0.8, aperture_wavelength=0.8):
        """
        Calculates the shift for each wavelength during an integration based on the observation details.
        
        This is dependent on two reference wavelengths:
            1) the guide wavelength - the wavelength the telescope guides on, which remains fixed on the focal plane.
            2) the aperture wavelength - the wavelength of the dispersed light that the aperture centre is positioned on. 
        
        Shifts are calculated using the Fillipenko 1982 model.
        
        This function must come after ``load_wavelengths`` and ``load_observation``
        
        :param guide_wavelength: The observation's guide wavelength, in units of micrometers. Default = 0.8um.
        :type guide_wavelength: float
        :param aperture_wavelength: The wavelength of the dispersed light that the aperture centre is positioned on, in units of micrometers - by default this refers to the dispersion half-way through the observation. Default = 0.8um.
        :type guide_wavelength: float
        """
        self.input['guide_wavelength']=guide_wavelength
        self.input['aperture_wavelength']=aperture_wavelength

        airmasses=self.output['airmasses']
        wavelengths=self.output['wavelengths']

        #centring refers to the index of the hour angles at which we centre the aperture/guiding on a wavelength
        if float(self.config['centring']) == 0.5:
            centring_index=int((len(airmasses)-1)/2)
        else:
            centring_index=int(self.config['centring'])

        centre_shift=diff_func.diff_shift(aperture_wavelength,airmasses[centring_index],guide_wavelength,self.config) #shift of the original aperture centre wavelength from guide wavelength
        centring_q=self.output['raw_para_angles'][centring_index]

        raw_para_angles=self.output['raw_para_angles']
        para_angles=self.output['raw_para_angles'].copy()
        for i in range(0,len(para_angles)): #change in PAs from centring index
            para_angles[i]=para_angles[i]-self.output['raw_para_angles'][centring_index]

        shifts_para=[]
        phi=np.deg2rad(float(self.config['relative_plate_PA_angle']))
        for count,airmass in enumerate(airmasses): #for each airmass, calculate AD shift
            shift_vals=diff_func.diff_shift(wavelengths,airmass,guide_wavelength,self.config)  
            airmass_shifts=[]

            for i in range(0,len(shift_vals)):
                x=(shift_vals[i])*np.sin(raw_para_angles[count])-centre_shift*np.sin(centring_q)
                y=(shift_vals[i])*np.cos(raw_para_angles[count])-centre_shift*np.cos(centring_q)
                airmass_shifts.append([x*np.cos(phi)-y*np.sin(phi),y*np.cos(phi)+x*np.sin(phi)])
                
            shifts_para.append(airmass_shifts)

        self.output['shifts']=np.array(shifts_para)
        centre_shift_para=[-centre_shift*np.sin(centring_q),-centre_shift*np.cos(centring_q)]
        centre_shift_para=[centre_shift_para[0]*np.cos(phi)-centre_shift_para[1]*np.sin(phi),
                           centre_shift_para[1]*np.cos(phi)+centre_shift_para[0]*np.sin(phi)]
        self.output['centre_shift']=centre_shift_para
        
    def load_aperture(self,aperture_major_axis=0.6,aperture_type="circle",hexagon_radius=1):
        """
        Define the spectrograph aperture.
        
        :param aperture_major_axis: Length of the aperture's major axis, units of arcseconds. Default = 0.6 arcsec.
        :type aperture_major_axis: float
        :param aperture_type: Aperture shape to use in the simulation. Currently can be one of "hexagons", "circle", (WIP: slit, square). Default = "circle".
        :type aperture_type: string
        :param hexagon_radius: If aperture is "hexagons", the number of rings in the hexagonally packed array. Default = 1.
        :type hexagon_radius: int
        """
        self.input['aperture_major_axis']=aperture_major_axis
        aperture=diff_func.make_aperture(aperture_type,aperture_major_axis,self.config,hexagon_radius=hexagon_radius)
        self.output['aperture']=aperture
             
    def load_PSFs(self,PSF_type="moffat",moffat_beta=2.5):
        """
        Define and generate the PSFs. These will be generated with airmass and wavelength dependences and are needed for the transmission calculations.
        
        This function must come after ``load_wavelengths``, ``load_observation``, ``load_aperture``, and ``calculate_integration_shifts``.
        
        :param PSF_type: PSF form to use in the simulations. Can be one of "moffat", "gaussian". Default = "moffat"
        :type PSF_type: string
        :param moffat_beta: Power value of the moffat PSF. Default = 2.5
        :type moffat_beta: float
        """
        self.input['PSF_type']=PSF_type
        all_PSFs=[]
        all_aligned_PSFs=[]
        
        zero_shifts=np.zeros(np.shape(self.output['shifts'][0]))

        for i in range(0,len(self.output['airmasses'])):
            PSFs=diff_func.make_PSFs(PSF_type,self.output['wavelengths'],self.output['shifts'][i],
                                                        self.output['airmasses'][i],self.input['aperture_major_axis'],self.config,beta=moffat_beta)
            aligned_PSFs=diff_func.make_PSFs(PSF_type,self.output['wavelengths'],zero_shifts,
                                                          self.output['airmasses'][i],self.input['aperture_major_axis'],self.config,beta=moffat_beta)
            all_PSFs.append(PSFs)
            all_aligned_PSFs.append(aligned_PSFs)

        self.output['PSFs']=all_PSFs
        self.output['aligned_PSFs']=all_aligned_PSFs
        
    def calculate_integration_transmissions(self):
        """
        Numerically calculates the transmissions values.
        
        This function must come after ``load_wavelengths``, ``load_observation``, ``load_aperture``, ``calculate_integration_shifts``, and ``load_PSFs``.
        """
        convolved_arrays=self.output['PSFs']*self.output['aperture']
        convolved_aligned_arrays=self.output['aligned_PSFs']*self.output['aperture']
        self.output['PSFs_through_aperture']=convolved_arrays
        self.output['aligned_PSFs_through_aperture']=convolved_aligned_arrays

        raw_transmissions=np.sum(convolved_arrays,axis=(-1,-2))
        no_AD_transmissions=np.sum(convolved_aligned_arrays,axis=(-1,-2))
        relative_transmissions=raw_transmissions/no_AD_transmissions
        self.output['raw_transmissions']=raw_transmissions
        self.output['no_AD_transmissions']=no_AD_transmissions
        self.output['relative_transmissions']=relative_transmissions

        relative_integration_transmissions=np.mean(relative_transmissions,axis=0)
        no_AD_integration_transmissions=np.mean(no_AD_transmissions,axis=0)
        raw_integration_transmissions=np.mean(raw_transmissions,axis=0)
        self.output['raw_integration_transmissions']=raw_integration_transmissions
        self.output['no_AD_integration_transmissions']=no_AD_integration_transmissions
        self.output['relative_integration_transmissions']=relative_integration_transmissions

    def integration_plots(self,y_axis='relative',track_indexes=[0,-1]):
        """
        Illustrates simulation results with two graphs:
            1) Transmission vs wavelength curves for individual fibres and entire bundle.
            2) Track plot of monochromatic spot PSFs on the aperture over an integration.
        
        This function must come after calculate_integration_transmissions
        
        :param y_axis: The y-axis of the transmission plot can be relative to either raw transmissions or no atmospheric-dispersion transmissions. Options are "raw" or "relative" respectively. Default = "relative".
        :type y_axis: string
        :param track_indexes: indexes of the wavelengths to use for the track plot. Default = [0,-1].
        :type track_indexes: list of int
        """
        plt.style.use('bmh')
        fig=plt.figure(figsize=[7,5])
        if y_axis=='relative':
            y_axis_data=self.output['relative_integration_transmissions']
            plt.axhline(y=1,label='No AD Transmission, {}'.format(self.input['PSF_type']),color='black',linestyle='--')
            plt.ylabel("Transmission Relative to No-AD")
        if y_axis=='raw':
            y_axis_data=self.output['raw_integration_transmissions']
            plt.ylabel("Raw Transmission")
            plt.plot(self.output['wavelengths'],self.output['no_AD_integration_transmissions'],color='black',linestyle='--',label='No AD Transmission, {}'.format(self.input['PSF_type']))
            
        plt.axvline(self.input['guide_wavelength'],label="Guide = {}um".format(self.input['guide_wavelength']),color='black',linestyle='--',linewidth=0.5)
        plt.axvline(self.input['aperture_wavelength'],label="Aperture = {}um".format(self.input['aperture_wavelength']),color='C0',linestyle='--',linewidth=0.5)
        plt.plot(self.output['wavelengths'],y_axis_data)
        plt.ylim(0,1.1)
        plt.xlabel("Wavelength (um)")
        plt.legend()
        
        fig, ax = plt.subplots(figsize=[5,5]) 
        weights = np.linspace(0, len(self.output['wavelengths'])-1,len(track_indexes))
        norm = mpl.colors.Normalize(vmin=min(weights), vmax=max(weights))
        cmap = mpl.cm.ScalarMappable(norm=norm, cmap='seismic')
        circle1 = plt.Circle((0, 0), self.input['aperture_major_axis']/2, color='black', fill=False, label='Major Axis')
        ax.add_patch(circle1)    
        plt.axvline(0,color='black',linestyle='--',linewidth=0.7,label="PA = {}".format(self.config['relative_plate_PA_angle']))
        plt.scatter(self.output['centre_shift'][0],self.output['centre_shift'][1],label='Guide = {}um'.format(self.input['guide_wavelength']),color='black',marker='+')
        plt.xlim(-0.4,0.4)
        plt.ylim(-0.4,0.4)
        shifts=self.output['shifts']
        for count,i in enumerate(track_indexes):
            xs,ys=[],[]
            for o in range(0,len(shifts)):
                xs.append(shifts[o][i][0])
                ys.append(shifts[o][i][1]) 
            plt.plot(xs,ys,marker='x',color=cmap.to_rgba(weights[count]),label="{}um".format(round(self.output['wavelengths'][i],4)))
        plt.legend()
        plt.xlabel("x (arcsec)")
        plt.ylabel("y (arcsec)")
    
    def run(self,observation_start=0,observation_end=1,declination=-30,wavelengths=[],aperture_major_axis=[],guide_wavelength=0,aperture_wavelength=0,**kwargs):
        """
        A simple in-built (but limited) atmospheric dispersion simulation.
        
        The guide and aperture will be optimised to the nearest 0.1um if values are not input.
        The simulation in this setup is a circular fibre with atmopsheric moffat PSFs.

        :param observation_start: Start of the observation in terms of hour angles, default = 0h.
        :type observation_start: float
        :param observation_end: End of the observation in terms of hour angles, default = 1h.
        :type observation_end: float
        :param declination: Declination of the observation target, in degrees. Default = -30 deg.
        :type declination: float
        :param wavelengths: Wavelengths to calculate transmission for, units of micrometers (um).
        :type wavelengths: list of float
        :param aperture_major_axis: Length of the aperture's major axis, units of arcseconds. Default = 0.6 arcsec.
        :type aperture_major_axis: float
        :param guide_wavelength: The observation's guide wavelength, in units of micrometers. Default = 0 - automatically optimised.
        :type guide_wavelength: float
        :param aperture_wavelength: The wavelength of the dispersed light that the aperture centre is positioned on, in units of micrometers - by default this refers to the dispersion half-way through the observation. Default = 0: automatically optimised.
        :type guide_wavelength: float
        """
        self.config.update(kwargs)
        self.load_observation(observation_start=observation_start,observation_end=observation_end,declination=declination)
        self.load_wavelengths(wavelengths=wavelengths)
        self.load_aperture(aperture_major_axis=aperture_major_axis,aperture_type="circle")
        if guide_wavelength==0 or aperture_wavelength ==0:
            print("Optimising Guide/Aperture Wavelength")
            self.optimise_integration(np.arange(wavelengths[0],wavelengths[-1],0.1),np.arange(wavelengths[0],wavelengths[-1],0.1),guide_aperture="equal")
            print("Optimal Guide/Aperture = {}um (nearest 0.1um)".format(self.input['guide_wavelength']))
        else:
            self.calculate_integration_shifts(guide_wavelength=guide_wavelength,aperture_wavelength=aperture_wavelength)
            self.load_PSFs()
            self.calculate_integration_transmissions()
        self.integration_plots()
            
    def optimise_integration(self,guide_options=[],aperture_options=[],guide_aperture="equal"):
        """
        Optimise the aperture and guide wavelengths. The metric optimised is the transmission curve's minimum multiplied by the throughput squared.
        
        This function must come after load_wavelengths, load_observation, and load_aperture
        
        :param guide_wavelength: The possible observation's guide wavelengths, in units of micrometers.
        :type guide_wavelength: list of float
        :param aperture_wavelength: The possible wavelengths of the dispersed light that the aperture centre is positioned on, in units of micrometers - by default this refers to the dispersion half-way through the observation.
        :type guide_wavelength: list of float
        :param guide_aperture: Determines whether the guide and aperture wavelengths are independent or are set to be equal, options are "independent" or "equal" respectively. Default = "equal"
        :type guide_aperture: string
        """
        
        if guide_aperture=="independent":
            metrics=np.zeros((len(guide_options),len(aperture_options),3))
            performance_metrics=np.zeros((len(guide_options),len(aperture_options),3))
            best_performance_metric=0
            for guide_count,guide in enumerate(guide_options):
                for aperture_count,aperture in enumerate(aperture_options):
                    self.calculate_integration_shifts(guide_wavelength=guide,aperture_wavelength=aperture)
                    self.load_PSFs()
                    self.calculate_integration_transmissions()
                    metric=diff_func.integ_metrics(self.output['relative_integration_transmissions'])
                    
                    metrics[guide_count][aperture_count]=metric
                    performance_metric=metrics[guide_count][aperture_count][0]*metrics[guide_count][aperture_count][2]**2
                    performance_metrics[guide_count][aperture_count]=performance_metric
                    
                    if performance_metric > best_performance_metric:
                        best_performance_metric=performance_metric
                        best_guide=guide
                        best_aperture=aperture
                        best_metric=metric
                        
        if guide_aperture=="equal":
            metrics=np.zeros((len(guide_options),3))
            performance_metrics=np.zeros((len(guide_options),3))
            best_performance_metric=0
            for guide_count,guide in enumerate(guide_options):
                self.calculate_integration_shifts(guide_wavelength=guide,aperture_wavelength=guide)
                self.load_PSFs()
                self.calculate_integration_transmissions()
                metric=diff_func.integ_metrics(self.output['relative_integration_transmissions'])
                
                metrics[guide_count]=metric
                performance_metric=metrics[guide_count][0]*metrics[guide_count][2]**2
                performance_metrics[guide_count]=performance_metric
                
                if performance_metric > best_performance_metric:
                    best_performance_metric=performance_metric
                    best_guide=guide
                    best_aperture=guide
                    best_metric=metric  
        
        print("Optimal Metrics:")
        print("Min Transmission = {}%".format(round(best_metric[0]*100)))
        print("Max Transmission = {}%".format(round(100*best_metric[1])))
        print("Throughput = {}%".format(round(100*best_metric[2])))
         
        self.calculate_integration_shifts(round(best_guide,5),round(best_aperture,5))
        self.load_PSFs()
        self.calculate_integration_transmissions()
 
        return
    
    def load_ZA(self, ZA_range=[]):
        """
        """
        airmasses=diff_func.ZA_to_airmass(ZA_range)
        self.output['airmasses']=airmasses
        self.input['ZA_range']=ZA_range
    
    def calculate_snapshot_shifts(self,aperture_wavelength):
        """
        """
        self.input['aperture_wavelength']=aperture_wavelength
    
        airmasses=self.output['airmasses']
        wavelengths=self.output['wavelengths']
        
        shifts=[]
        for count,airmass in enumerate(airmasses):
            centre_shift=diff_func.diff_shift(aperture_wavelength,airmass,1,self.config)
            airmass_shifts=diff_func.diff_shift(wavelengths,airmass,1,self.config)-centre_shift
            airmass_shifts=np.append(np.resize(airmass_shifts,(len(airmass_shifts),1)),np.zeros((len(airmass_shifts),1)),axis=-1)
            shifts.append(airmass_shifts)
        self.output['shifts']=shifts
        
    def calculate_snapshot_transmissions(self):
        """
        """
        convolved_arrays=self.output['PSFs']*self.output['aperture']
        convolved_aligned_arrays=self.output['aligned_PSFs']*self.output['aperture']
        self.output['PSFs_through_aperture']=convolved_arrays
        self.output['aligned_PSFs_through_aperture']=convolved_aligned_arrays

        raw_transmissions=np.sum(convolved_arrays,axis=(-1,-2))
        no_AD_transmissions=np.sum(convolved_aligned_arrays,axis=(-1,-2))
        relative_transmissions=raw_transmissions/no_AD_transmissions
        self.output['raw_transmissions']=raw_transmissions
        self.output['no_AD_transmissions']=no_AD_transmissions
        self.output['relative_transmissions']=relative_transmissions
        
    def snapshot_plots(self,y_axis='relative'):
        """
        """
        plt.style.use('bmh')
        fig=plt.figure(figsize=[7,5])
        if y_axis=='relative':
            y_data=self.output['relative_transmissions']
            plt.axhline(y=1,label='No AD Transmission, {}'.format(self.input['PSF_type']),color='black',linestyle='--')
            plt.ylabel("Transmission Relative to No-AD")
        if y_axis=='raw':
            y_data=self.output['raw_transmissions']
            plt.ylabel("Raw Transmission")
        
        plt.axvline(self.input['aperture_wavelength'],label="Aperture = {}um".format(self.input['aperture_wavelength']),color='C0',linestyle='--',linewidth=0.5)
        for count,trans in enumerate(y_data):
            plt.plot(self.output['wavelengths'],trans,label="ZA = {} deg".format(round(self.input['ZA_range'][count],1)))
        plt.ylabel("Transmission Relative to No-AD")
        plt.ylim(0,1.1)
        plt.xlabel("Wavelength (um)")
        plt.legend()   