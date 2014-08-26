#!/bin/bash

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

if [ -f ../../../pyslic/bin/activate ];
then
	source ../../../pyslic/bin/activate
fi
 
wget -nc http://murphylab.web.cmu.edu/data/cho/giantin.tgz
wget -nc http://murphylab.web.cmu.edu/data/cho/hoechst.tgz 
wget -nc http://murphylab.web.cmu.edu/data/cho/lamp2.tgz 
wget -nc http://murphylab.web.cmu.edu/data/cho/nop4.tgz
wget -nc http://murphylab.web.cmu.edu/data/cho/tubulin.tgz

for FILE in *.tgz
do
	tar -xvf "$FILE"
	rm -f "$FILE"
done

find . -name ".DS_Store" -exec rm -fv {} \;

python calculate_features.py
find . -name "*.pkl"

if [ -f ../../../pyslic/bin/activate ];
then
	deactivate
fi