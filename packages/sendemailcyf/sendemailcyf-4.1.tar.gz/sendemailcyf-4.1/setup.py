from distutils.core import  setup
import setuptools
packages = ['sendemailcyf']               # 唯一的包名，自己取名
setup(name='sendemailcyf',
	version='4.1',
	author='CYF',
    packages=packages, 
    package_dir={'requests': 'requests'},)