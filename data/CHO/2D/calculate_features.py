# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from os import walk
from os import path
from os import chdir
import Image
import numpy
import pyslic
import cPickle as pickle

#SLF33 feature ids
feature_ids = ["SLF27.66","SLF27.67","SLF27.68","SLF27.69","SLF27.70","SLF27.71","SLF27.72","SLF27.73","SLF27.74","SLF27.75","SLF27.76","SLF27.77","SLF27.78","SLF33.37","SLF33.38","SLF33.39","SLF33.40","SLF33.41","SLF33.42","SLF33.43","SLF33.44","SLF33.45","SLF33.46","SLF33.47","SLF33.48","SLF33.49","SLF33.50","SLF33.51","SLF33.52","SLF33.53","SLF33.54","SLF33.55","SLF33.56","SLF33.57","SLF33.58","SLF33.59","SLF33.60","SLF33.61","SLF33.62","SLF33.63","SLF33.64","SLF33.65","SLF33.66","SLF33.67","SLF33.68","SLF33.69","SLF33.70","SLF33.71","SLF33.72","SLF33.73","SLF33.74","SLF33.75","SLF33.76","SLF33.77","SLF33.78","SLF33.79","SLF33.80","SLF33.81","SLF33.82","SLF33.83","SLF33.84","SLF33.85","SLF33.86","SLF33.87","SLF33.88","SLF33.89","SLF33.90","SLF33.91","SLF33.92","SLF33.93","SLF33.94","SLF33.95","SLF33.96","SLF33.97","SLF33.98","SLF33.99","SLF33.100","SLF33.101","SLF33.102","SLF33.103","SLF33.104","SLF33.105","SLF33.106","SLF33.107","SLF33.108","SLF33.109","SLF33.110","SLF33.111","SLF33.112","SLF33.113","SLF33.114","SLF27.1","SLF27.2","SLF27.3","SLF27.4","SLF27.5","SLF27.89","SLF27.90","SLF27.9","SLF27.10","SLF27.11","SLF27.12","SLF27.13","SLF27.80","SLF27.81","SLF27.82","SLF27.83","SLF27.84","SLF27.79","SLF31.1","SLF31.2","SLF31.3","SLF31.4","SLF31.5","SLF31.6","SLF31.7","SLF31.8","SLF31.9","SLF31.10","SLF31.11","SLF31.12","SLF31.13","SLF31.14","SLF31.15","SLF31.16","SLF31.17","SLF31.18","SLF33.1","SLF33.2","SLF33.3","SLF33.4","SLF33.5","SLF33.6","SLF33.7","SLF33.8","SLF33.9","SLF33.19","SLF33.20","SLF33.21","SLF33.22","SLF33.23","SLF33.24","SLF33.25","SLF33.26","SLF33.27","SLF33.10","SLF33.11","SLF33.12","SLF33.13","SLF33.14","SLF33.15","SLF33.16","SLF33.17","SLF33.18","SLF33.28","SLF33.29","SLF33.30","SLF33.31","SLF33.32","SLF33.33","SLF33.34","SLF33.35","SLF33.36","SLF34.1","SLF34.2","SLF34.3","SLF34.4","SLF34.5","SLF34.6","SLF34.7","SLF34.8","SLF34.9","SLF34.10","SLF27.80","SLF27.81","SLF27.82","SLF27.83","SLF27.84","SLF27.79","SLF27.1","SLF27.2","SLF27.3","SLF27.4","SLF27.5","SLF27.6","SLF27.7","SLF27.8","SLF27.85","SLF27.86","SLF27.87","SLF27.88","SLF27.89","SLF27.90","SLF27.14","SLF27.15","SLF27.16","SLF27.17","SLF27.18","SLF27.19","SLF27.20","SLF27.21","SLF27.22","SLF27.23","SLF27.24","SLF27.25","SLF27.26","SLF27.27","SLF27.28","SLF27.29","SLF27.30","SLF27.31","SLF27.32","SLF27.33","SLF27.34","SLF27.35","SLF27.36","SLF27.37","SLF27.38","SLF27.39","SLF27.40","SLF27.41","SLF27.42","SLF27.43","SLF27.44","SLF27.45","SLF27.46","SLF27.47","SLF27.48","SLF27.49","SLF27.50","SLF27.51","SLF27.52","SLF27.53","SLF27.54","SLF27.55","SLF27.56","SLF27.57","SLF27.58","SLF27.59","SLF27.60","SLF27.61","SLF27.62","SLF27.63","SLF27.64","SLF27.65","SLF27.66","SLF27.67","SLF27.68","SLF27.69","SLF27.70","SLF27.71","SLF27.72","SLF27.73","SLF27.74","SLF27.75","SLF27.76","SLF27.77","SLF27.78","SLF27.9","SLF27.10","SLF27.11","SLF27.12","SLF27.13","SLF31.1","SLF31.2","SLF31.3","SLF31.4","SLF31.5","SLF31.6","SLF31.7","SLF31.8","SLF31.9","SLF31.10","SLF31.11","SLF31.12","SLF31.13","SLF31.14","SLF31.15","SLF31.16","SLF31.17","SLF31.18"]

directories = [ x[0] for x in walk('.') ]

for directory in directories:
	if directory is not '.':
		chdir( directory )
		for (filepath, directories, filenames) in walk( '.' ):
			for filename in filenames:
				filename = path.join( filepath, filename )
				print filename
				[basename, extension] = path.splitext(filename)

				if extension == '.tif':
					features_filename = basename + '.pkl'
					pixels = Image.open(filename)
					pixels = numpy.array(pixels)
				
					#make pyslic image container
    					img=pyslic.Image()
    					img.label=basename
    					img.scale=0.237

    					img.channels[ 'protein' ] = 0
					img.channeldata[ 'protein' ] = pixels

        				img.loaded=True
					features = pyslic.computefeatures(img,'field+')
					image = {}
					image['pixels']=pixels
					image['scale']=img.scale
					image['label']=img.label
					image['feature_set']='SLF33'
					image['feature_ids']=feature_ids
					image['features']=features
				
					pickle.dump(image, open(features_filename,'w'))
		chdir( '../' )					
