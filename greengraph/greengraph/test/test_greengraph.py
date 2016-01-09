# TESTING
#---------------------
# Description: This code contains automated tests with nose.tools asserts to test every instance of the greengraph code.

# Usage: Run with nose from command line.

from nose.tools import assert_raises
from nose.tools import assert_in
from mock import patch
import yaml
import os
import sys
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

yml_filename = os.path.join(os.path.join(os.path.dirname(__file__), 'fixtures/sample.yml'))

# Open fixtures files
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



# Test input of parameters and prevent call to internet


def test_negative_steps():
    with assert_raises(ValueError) as exception:
        mygraph = Greengraph(sample_start, sample_end, sample_delay)
        data = mygraph.green_between(bad_sample_steps)

#def test_url_params():
#    assert_in('http://maps.googleapis.com/maps/api/staticmap?',url)
#    assert_in('center=51.5072%2C-0.1275',url)
#    assert_in('zoom=10',url)
#    assert_in('size=400x400',url)
#    assert_in('sensor=false',url)

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

# Testing specific functions from Greengraph class
#def test_delay():
#    delay_map = Greengraph(sample_start, sample_end, sample_delay)
#    no_delay_map = Greengraph(sample_start, sample_end, 0)
#    t1 = timeit.timeit(delay_map.geolocate(sample_start))
#    t2 = timeit.timeit(no_delay_map.geolocate(sample_start))
#    assert_true(t1 > t2)

def test_request_call():
    with patch.object(requests, 'get') as mock_get:
        with patch.object(img, 'imread') as mock_img: # Ensure Map class does not try and create pixel map from mock
            sample_map = Greengraph(sample_start, sample_end, sample_delay)
            test_place = Map(*sample_map.geolocate(sample_start))
            mock_get.assert_called_with('http://maps.googleapis.com/maps/api/staticmap?',params =  url)


def test_API_overload():
    test_list = [5000]*20
    test_list[2] = 323
    test_list[15] = 323
    with patch.object(Greengraph, 'green_between') as mock:
        mock.return_value = test_list
        test_map = Greengraph(sample_start, sample_end, sample_delay)
        assert (test_map.api_overload(sample_steps))==True
