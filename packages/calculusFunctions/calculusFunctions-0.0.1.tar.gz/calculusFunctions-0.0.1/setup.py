from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 1 - Planning',
  'Intended Audience :: Education',
  'Operating System :: MacOS',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='calculusFunctions',
  version='0.0.1',
  description='basic functions for calculus',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Preston Nemeti',
  author_email='prestonnemeti@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='calculus', 
  packages=find_packages(),
  install_requires=[''] 
)