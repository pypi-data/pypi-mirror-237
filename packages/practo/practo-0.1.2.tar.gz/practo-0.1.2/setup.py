from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='practo',
  version='0.1.2',
  description='It contains Algorithms',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  long_description_content_type="text/markdown",
  url='',  
  author='Hemanshu Pathak',
  author_email='himanshu2002pathak@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='algorithms', 
  packages=find_packages(),
  install_requires=[''] 
)