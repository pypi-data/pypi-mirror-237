import io
from os.path import abspath, dirname, join
from setuptools import find_packages, setup


HERE = dirname(abspath(__file__))
LOAD_TEXT = lambda name: io.open(join(HERE, name), encoding='UTF-8').read()
DESCRIPTION = '\n\n'.join(LOAD_TEXT(_) for _ in [
    'README.rst'
])

setup(
  name = 'OCR_GLS_G6',      
  packages = ['OCR_GLS_G6'], 
  version = '0.0.4',  
  license='MIT', 
  description = 'OCR_GLS_G6 - Optical character recognition and QR codes',
  long_description=DESCRIPTION,
  author = 'Burin Panchat',                 
  author_email = 'burin.gbp@gmail.com',     
  url = 'https://git.bdms.co.th/Burin.Pa/ocr_gls_g6',  
  download_url = 'https://git.bdms.co.th/Burin.Pa/ocr_gls_g6/-/archive/v0.0.4/ocr_gls_g6-v0.0.3.zip',  
  keywords = ['OCR_GLS_G6', 'OCR', 'ocr'],   
  classifiers=[
    'Development Status :: 3 - Alpha',     
    'Intended Audience :: Developers',     
    'Topic :: Documentation',
    'License :: OSI Approved :: MIT License',        
    'Programming Language :: Python :: 3.7',
  ],
  install_requires=[
          "certifi==2023.7.22",
          "cffi==1.15.1",
          "charset-normalizer==3.3.0",
          "clr-loader==0.2.6",
          "easyocr==1.7.1",
          "idna==3.4",
          "imageio==2.31.2",
          "IronPdf==2023.8.6",
          "networkx==2.6.3",
          "ninja==1.11.1.1",
          "numpy==1.21.6",
          "opencv-python==4.8.1.78",
          "opencv-python-headless==4.8.1.78",
          "packaging==23.2",
          "Pillow==9.5.0",
          "pyclipper==1.3.0.post5",
          "pycparser==2.21",
          "python-bidi==0.4.2",
          "pythonnet==3.0.3",
          "PyWavelets==1.3.0",
          "PyYAML==6.0.1",
          "pyzbar==0.1.9",
          "requests==2.31.0",
          "scikit-image==0.19.3",
          "scipy==1.7.3",
          "shapely==2.0.2",
          "six==1.16.0",
          "tifffile==2021.11.2",
          "torch==1.13.1",
          "torchvision==0.14.1",
          "typing_extensions==4.7.1",
          "urllib3==1.26.6",
      ],
)