from distutils.core import  setup
import setuptools
packages = ['unisearch']               # 唯一的包名，自己取名
setup(name='unisearch',
	version='1.2',
	author='CYF',
    packages=packages, 
    package_dir={'requests': 'requests'},)