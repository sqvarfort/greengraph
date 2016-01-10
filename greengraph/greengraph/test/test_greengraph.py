# TESTING
#---------------------
# Description: This code contains automated tests with nose.tools asserts to test every instance of the greengraph code.

# Usage: Run with nosetests from command line.

from nose.tools import assert_raises
from nose.tools import assert_in
from mock import patch
import yaml
import os
import sys
from geopy import geocoders
from PIL import Image
from StringIO import StringIO
from matplotlib import image as img
import matplotlib.pyplot as plt
import numpy as np
import requests
import timeit


# Import class to be tested
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from graph import Greengraph
from map import Map


# Open fixtures files
yml_filename = os.path.join(os.path.join(os.path.dirname(__file__), 'fixtures/fixtures.yml'))
with open(yml_filename) as f:
    fixtures = yaml.load(f)

# Allocate values
sample_start = fixtures[0]['sample_start']
sample_end = fixtures[0]['sample_end']
sample_steps = int(fixtures[0]['sample_steps']) # Make sure is integer
sample_filename = fixtures[0]['sample_filename']
sample_delay = int(fixtures[0]['sample_delay']) # Make sure is integer

url = fixtures[1]

bad_sample_start = fixtures[2]['bad_sample_start']
bad_sample_end = fixtures[2]['bad_sample_end']
bad_sample_steps = int(fixtures[2]['bad_sample_steps'])
bad_sample_filename = fixtures[2]['bad_sample_filename']
bad_sample_delay = int(fixtures[2]['bad_sample_delay'])


# INPUT
#-------------
# The following tests are concerned with the user input to greengraph. Each bad input is supposed to raise an exception, which these tests will look for.

def test_negative_steps():
    with assert_raises(ValueError) as exception:
        mygraph = Greengraph(sample_start, sample_end, sample_delay)
        data = mygraph.green_between(bad_sample_steps)

def test_bad_image_extension():
    with assert_raises(ValueError) as exception:
        mygraph = Greengraph(sample_start, sample_end, sample_delay)
        data = mygraph.green_between(sample_steps)
        plt.savefig(bad_sample_filename)

def test_negative_delay_input():
    with assert_raises(ValueError) as exception:
        Greengraph(sample_start, sample_end, bad_sample_delay)

def test_bad_start():
    with assert_raises(TypeError) as exception:
        mymap = Greengraph(bad_sample_start, sample_end, sample_delay)
        test = mymap.green_between(sample_steps)

def test_bad_end():
    with assert_raises(TypeError) as exception:
        mymap = Greengraph(sample_start, bad_sample_end, sample_delay)
        test = mymap.green_between(sample_steps)


# TESTING METHODS
#------------------------
# The following tests concern testing specific methods of the class.

def test_request_call():
    with patch.object(requests, 'get') as mock_get:
        with patch.object(img, 'imread') as mock_img: # Ensure Map class does not try and create pixel map from mock
            sample_map = Greengraph(sample_start, sample_end, sample_delay)
            test_place = Map(*sample_map.geolocate(sample_start))
            print mock_get.mock_calls
            mock_get.assert_called_with('http://maps.googleapis.com/maps/api/staticmap?',params =  url)

def test_API_overload():
    test_list = [5000]*20 # Create test array
    test_list[2] = 323 # Create two points which contain the critical value
    test_list[15] = 323
    with patch.object(Greengraph, 'green_between') as mock:
        mock.return_value = test_list
        test_map = Greengraph(sample_start, sample_end, sample_delay)
        assert (test_map.api_overload(sample_steps))==True


def test_geolocate():
    with patch.object(geocoders, 'GoogleV3') as mock_get:
        mymap = Greengraph(sample_start, sample_end, sample_delay)
        mymap.geolocate(sample_start)
        print mock_get.mock_calls
        mock_get.assert_called_with(domain='maps.google.co.uk')



#UNCOMPLETED TESTS
#----------------------

# Testing specific functions from Greengraph class
#def test_delay():
#    delay_map = Greengraph(sample_start, sample_end, sample_delay)
#    no_delay_map = Greengraph(sample_start, sample_end, 0)
#    t1 = timeit.timeit(delay_map.geolocate(sample_start))
#    t2 = timeit.timeit(no_delay_map.geolocate(sample_start))
#    assert_true(t1 > t2)


#def test_green():
    # Fetch test image path
#green_img_path = os.path.join(os.path.join(os.path.dirname(__file__), 'test_img/green_image.png'))
#green_image = Image.open(green_img_path)
#test_object = Greengraph(sample_start, sample_end, sample_delay)
#test_map = Map(*test_object.geolocate(sample_start))
#test_map.image = green_image
#print type(test_map.image)
#test_map.pixels = img.imread(IOStream(test_map.image)
    #green_count = test_map.count_green()
