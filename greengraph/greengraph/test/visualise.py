# VISUALISATION
#--------------------------
# Description: This program visualises the maps obtained at different instances by the greengraph.py program. The purpose of this program is to provide the user with a tool that allows the visualisation of the maps used for counting in the program. 

# Usage: Run program. Maps of the start and end locations will be shown as aerial photographs and as pixel maps of all green pixels.

import os
import sys
from PIL import Image
from StringIO import StringIO
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from graph import Greengraph
from map import Map
import yaml

# Import fixtures from file and dump into fixtures
yml_filename = os.path.join(os.path.join(os.path.dirname(__file__), 'fixtures/sample.yml'))
with open(yml_filename) as f:
    fixtures = yaml.load(f)


sample_start = fixtures[0]['sample_start']
sample_end = fixtures[0]['sample_end']
sample_steps = int(fixtures[0]['sample_steps']) # Make sure is integer
sample_filename = fixtures[0]['sample_filename']
sample_delay = int(fixtures[0]['sample_delay']) # Make sure is integer

some_map = Greengraph(sample_start, sample_end, sample_delay)
img_start = Image.open(StringIO(some_map.show_map(sample_start)))
img_end = Image.open(StringIO(some_map.show_map(sample_end)))
img_start.show()
img_end.show()

# Show green pixel maps

img_green_start = Image.open(StringIO(some_map.show_green_map(sample_start)))
img_green_end = Image.open(StringIO(some_map.show_green_map(sample_end)))
img_green_start.show()
img_green_end.show()




# Should we load the sample images into a folder?
#green_map = mymap.show_green()
#green_img = Image.open(StringIO(green_map.content))
#green_img.show()
#green_img.savefile('test_img/green_map.png')
