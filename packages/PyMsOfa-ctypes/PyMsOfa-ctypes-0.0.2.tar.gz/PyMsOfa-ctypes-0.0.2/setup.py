from setuptools import Extension,setup,find_packages
import glob

long_desc ='''
*PyMsOfa* is a `Python <http://www.python.org/>`_ module for accessing `International Astronomical Union <http://www.iau.org/>`_'s `SOFA library <http://www.iausofa.org/>`_ from Python. SOFA (Standards of Fundamental Astronomy) is a set of algorithms and procedures that implement standard models used in fundamental astronomy.

*PyMsOfa* is not a part of SOFA routines but a Python package for the SOFA C library. 

*PyMsOfa* is neither distributed, supported nor endorsed by the International Astronomical Union. In addition to *PyMsOfa*’s license, any use of this module should comply with `SOFA’s license and terms of use <http://www.iausofa.org/tandc.html>`_. Especially, but not exclusively, any published work or commercial products including results achieved by using *PyMsOfa* shall acknowledge that the SOFA software was used to obtain those results.

This version is a python wrapper package based on a foreign function library for Python (ctypes).

To cite PyMsOfa in publications use:

> 1.    Ji, Jiang-Hui, Tan, Dong-jie, Bao, Chun-hui, Huang, Xiu-min, Hu, Shoucun, Dong, Yao, Wang, Su. 2023, PyMsOfa: A Python Package for the Standards of Fundamental Astronomy (SOFA) Service, Research in Astronomy and Astrophysics, https://doi.org/10.1088/1674-4527/ad0499

> 2.	Ji, Jiang-Hui, Li, Hai-Tao, Zhang, Jun-Bo, Fang, Liang, Li, Dong, Wang, Su, Cao, Yang, Deng, Lei, Li, Bao-Quan, Xian, Hao, Gao, Xiao-Dong, Zhang, Ang, Li, Fei, Liu, Jia-Cheng, Qi, Zhao-Xiang,  Jin, Sheng, Liu, Ya-Ning, Chen, Guo, Li, Ming-Tao, Dong, Yao, Zhu, Zi, and CHES Consortium. 2022, CHES: A Space-borne Astrometric Mission for the Detection of Habitable Planets of the Nearby Solar-type Stars, Research in Astronomy and Astrophysics, 22, 072003

'''

sofa_lib = Extension("PyMsOfa.libsofa_c",
                       glob.glob('./C/*.c'),
                       depends=["./C/sofa.h", "./C/sofam.h"],
                       include_dirs=["./C"])
        
setup(
    name='PyMsOfa-ctypes',
    version='0.0.2',
    author='Ji,jianghui',
    author_email="jijh@pmo.ac.cn",
    description='a Python package for the Standards of Fundamental Astronomy (SOFA) service',
    long_description=long_desc,
    ext_modules = [sofa_lib],
    packages = find_packages(),
    license='MIT',   
    install_requires=[],
    include_package_data = True,
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
