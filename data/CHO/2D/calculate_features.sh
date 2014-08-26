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
	echo "Activating virtual environment"
	source ../../../pyslic/bin/activate
fi
 
echo "Downloading tarballs from Murphy Lab website"
wget -nc http://murphylab.web.cmu.edu/data/cho/giantin.tgz
wget -nc http://murphylab.web.cmu.edu/data/cho/hoechst.tgz 
wget -nc http://murphylab.web.cmu.edu/data/cho/lamp2.tgz 
wget -nc http://murphylab.web.cmu.edu/data/cho/nop4.tgz
wget -nc http://murphylab.web.cmu.edu/data/cho/tubulin.tgz

echo "Extracting tarballs"
for FILE in *.tgz
do
	tar -xf "$FILE"
	rm -f "$FILE"
done

echo "Delete unnecessary files from extracted tarball"
find . -name ".DS_Store" -exec rm -fv {} \;

echo "Calculate SLF33 feature set on downloaded images"
python calculate_features.py

echo "Lets try to find the pickle files containing the feature vectors"
find . -name "*.pkl"

if [ -f ../../../pyslic/bin/activate ];
then
	echo "Deactivating virtual environment"
	deactivate
fi
