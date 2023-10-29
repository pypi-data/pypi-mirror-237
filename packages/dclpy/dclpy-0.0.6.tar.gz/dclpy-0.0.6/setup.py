#!/bin/python
import subprocess
from distutils.core import setup, Extension

packagename = "dclpy"
dcllib=[]
pyinc=[]

output = subprocess.getoutput("dclconfig --ldlibs")
for token in output.strip().split():
    dcllib.append(token[2:])
#    kw.setdefault(flag_map.get(token[:2]), []).append(token[2:])
output = subprocess.getoutput("pkg-config --cflags python3")
for token in output.strip().split():
    pyinc.append(token)
#    kw.setdefault(flag_map.get(token[:2]), []).append(token[2:])

#print (libraries)
print (pyinc)

setup(
    name='dclpy',
    version='0.0.6',
    ext_modules = [
        Extension(
            'dclpy',
            ['dclpy/dclpy_wrapper.c'],
            libraries=dcllib,
            include_dirs=pyinc,
        ),
    ],
)
