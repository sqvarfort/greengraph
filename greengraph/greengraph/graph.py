import numpy as np
import geopy
import time
from map import Map
from PIL import Image
from StringIO import StringIO

# Create the Greengraph object
class Greengraph(object):
    def __init__(self, start, end, delay):
        self.start=start # Declare local variables
        self.end=end
        self.geocoder=geopy.geocoders.GoogleV3(domain="maps.google.co.uk")
        self.delay = delay
        if delay == None:
            self.delay = 0
        if self.delay < 0:
            raise ValueError('Delay must be a non-negative number.')
            quit()

    def geolocate(self, place): #Find the place
        time.sleep(self.delay) # Delay request
        try:
            geolocate_place = self.geocoder.geocode(place,exactly_one=False)[0][1]
            return  geolocate_place
        except TypeError:
            raise TypeError( 'Input "%s" not found.' %place)
            quit()


    def location_sequence(self, start,end,steps): # Return matrix with lats and longs
        lats = np.linspace(start[0], end[0], steps)
        longs = np.linspace(start[1],end[1], steps)
        return np.vstack([lats, longs]).transpose()

    def green_between(self, steps): # Returns a list with the number of green pixels in each satellite image
        if steps == None:
            steps = 20 #Default step size
        if steps <= 0: # Raise exception for non-positive values
            raise ValueError("Step size must be a positive number.")
        green_array = [Map(*location).count_green()
        for location in self.location_sequence(
        self.geolocate(self.start),
        self.geolocate(self.end),steps)]
        return green_array

    def api_overload(self, steps): # Return TRUE if API overload
        data = self.green_between(steps)
        error_threshold = 2
        count = 0
        for iterate in range(0,len(data)):
            if data[iterate] == 323:
                count += 1
        if count >= error_threshold:
            return True
        else:
            return False

    def show_map(self, place): # Access satellite image of Map object
        return Map(*self.geolocate(place)).image

    def show_green_map(self, place): # Access green pixel map
        some_map = Map(*self.geolocate(place))
        return some_map.show_green()
