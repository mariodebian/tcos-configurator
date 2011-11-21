#!/usr/bin/python
# -*- coding: UTF-8 -*-
#    TcosConfigurator version __VERSION__
#
# Copyright (c) 2006-2011 Mario Izquierdo <mariodebian@gmail.com>
#
# This package is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
#
# This package is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
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

data_files.append(('share/tcos-configurator', ['tcos-configurator.ui'] ))

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

