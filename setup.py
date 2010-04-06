#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 
# This script is inspired by the debian package python-chardet
import os
import glob
from distutils.core import setup
from distutils.command.build import build

data_files = []

def get_debian_version():
    f=open('debian/changelog', 'r')
    line=f.readline()
    f.close()
    version=line.split()[1].replace('(','').replace(')','')
    return version

class build_locales(build):
    os.system("cd po && make gmo")

for (path, dirs, files) in os.walk("po"):
    if "tcos-configurator.mo" in files:
        target = path.replace("po", "share/locale", 1)
        data_files.append((target, [os.path.join(path, "tcos-configurator.mo")]))

def get_images(ipath):
    images = []
    for afile in glob.glob('%s/*'%(ipath) ):
        if os.path.isfile(afile):
            images.append(afile)
    return images
        
data_files.append(('share/tcos-configurator/images', get_images("images") ))

data_files.append(('share/tcos-configurator', ['tcos-configurator.glade'] ))

data_files.append(('share/applications', ['tcos-configurator.desktop'] ))

setup(name='TcosConfigurator',
      description = 'Configure TCOS server services',
      version=get_debian_version(),
      author = 'Mario Izquierdo',
      author_email = 'mariodebian@gmail.com',
      url = 'http://www.tcosproject.org',
      license = 'GPLv2',
      platforms = ['linux'],
      keywords = ['thin client', 'teacher monitor', 'ltsp'],
      scripts=['tcos-configurator'],
      cmdclass = {'build': build_locales},
      data_files=data_files
      )

