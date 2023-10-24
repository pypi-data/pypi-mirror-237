import setuptools 
  
with open("README.md", "r") as fh: 
    description = fh.read() 
  
setuptools.setup( 
    name="atmosphyre", 
    version="0.0.6", 
    author="Jay Stephan", 
    author_email="Jay.Stephan@stfc.ac.uk", 
    packages=["atmosphyre"],  
    description="A Python package to characterise the impact of atmospheric dispersion on a spectrographs throughput.", 
    long_description=description, 
    long_description_content_type="text/markdown", 
    license='MIT', 
    install_requires=['numpy','astropy','matplotlib','scipy'] 
) 

