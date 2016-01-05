from graph import Greengraph
import map
from nose.tools import assert_raises
from mock import patch
import yaml

# Replace function of requests.get with mock

from fixtures import params, bad_params

def test_call_to_internet():
    with patch.object(requests, 'get') as mock_get:
        Map('London')
        print mock_get, mock_calls
        mock.get.assert_called_with("http://maps.googleapis.com/maps/api/staticmap?", params)


yaml.load(open('fixtures.yml'))

# This is a sample test
# Here we write methods for testing

def test_parameters():

def test_mock_parameters():

def test_mock_webaddress():


def test_filename_call():

def test_input():
    assert



def test_negative_steps_input():
    with assert_raises(ValueError) as exception:
        mygraph = Greengraph(sample_start, sample_end)
        data = mygraph.green_between(-20)




# Test reaction of same location
Greengraph('London', 'London')

# Assert that the correct parameters are obtained
from nose.tools import assert_in
assert_in("http://maps.googleapis.com/maps/api/staticmap?",url)
assert_in("center=51.5072%2C-0.1275",url)
assert_in("zoom=10",url)
assert_in("size=400x400",url)
assert_in("sensor=false",url)
