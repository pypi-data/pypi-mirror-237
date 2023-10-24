from distutils.core import setup
from setuptools import find_packages


long_desc ='''
*PyMsOfa* is a `Python <http://www.python.org/>`_ module for accessing `International Astronomical Union <http://www.iau.org/>`_'s `SOFA library <http://www.iausofa.org/>`_ from Python. SOFA (Standards of Fundamental Astronomy) is a set of algorithms and procedures that implement standard models used in fundamental astronomy.

*PyMsOfa* is not a part of SOFA routines but a Python package for the SOFA C library. Thus, no calculations are made into the PyMsOfa package based on ctypes and cffi interface, which are all delegated to the underlying SOFA C library.

*PyMsOfa* is neither distributed, supported nor endorsed by the International Astronomical Union. In addition to *PyMsOfa*’s license, any use of this module should comply with `SOFA’s license and terms of use <http://www.iausofa.org/tandc.html>`_. Especially, but not exclusively, any published work or commercial products including results achieved by using *PyMsOfa* shall acknowledge that the SOFA software was used to obtain those results.
'''

setup(
    name='PyMsOfa',
    version='1.0.1',
    author='Ji,jianghui',
    author_email="jijh@pmo.ac.cn",
    description='a Python package for the Standards of Fundamental Astronomy (SOFA) service',
    long_description=long_desc,
    # 使用find_packages()自动发现项目中的所有包
    packages=find_packages(),
    # 许可协议
    license='MIT',
    # 要安装的依赖包
    install_requires=[],
    # keywords=['python', 'menu', 'dumb_menu','windows','mac','linux'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.0",
        "Operating System :: Unix",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Scientific/Engineering :: Astronomy"
    ]
)
