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
        time.sleep(self.delay)
        try:
            return self.geocoder.geocode(place,exactly_one=False)[0][1]
        except TypeError: #Catch bad input locations
            print 'Input "%s" not found.' %place
            quit()

    def location_sequence(self, start,end,steps): #Denote the latitude/longitude
        lats = np.linspace(start[0], end[0], steps) # np.linspace returns evenly spaced numbers over an interval
        longs = np.linspace(start[1],end[1], steps)
        return np.vstack([lats, longs]).transpose()

# This returns an array with two values: the steps and the
    def green_between(self, steps):
        if steps == None:
            steps = 20 #Default step size
        if steps <= 0: # Raise exception for non-positive values
            raise ValueError("Step size must be a positive number.")
        green_array = [Map(*location).count_green()
        for location in self.location_sequence(
        self.geolocate(self.start),
        self.geolocate(self.end),steps)]
        return green_array
        #if type(green_array) == NoneType:
        #    raise ValueError('Input location not found')
        #    quit()

# Google API error method
    def api_overload(self, steps):
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

    def show_map(self, place):
        return Map(*self.geolocate(place)).image

    def show_green_map(self, place):
        some_map = Map(*self.geolocate(place))
        return some_map.show_green()





        #pixels=img.imread(StringIO(data)) # Get our PNG image as rows of pixels
        #green = is_green(pixels)
        #out = green[:,:,np.newaxis]*np.array([0,1,0])[np.newaxis,np.newaxis,:]
        #buffer = StringIO()
        #result = img.imsave(buffer, out, format='png')
        #return buffer.getvalue()
