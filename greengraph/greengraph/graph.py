import numpy as np
import geopy
import time
from map import Map

# This is the constructor
# Should we divide these two into two files? I would
# Create one map object and one greengraph object


# Create the Greengraph object
class Greengraph(object):
    def __init__(self, start, end, delay): #These is the main object that I create with the start and end location
        self.start=start # Declare local variables?
        self.end=end
        self.geocoder=geopy.geocoders.GoogleV3(domain="maps.google.co.uk")
        self.delay = delay
        if delay == None:
            self.delay = 0

        if self.delay < 0:
            raise ValueError('Delay must be a non-negative number.')
            quit()

         #Create object, geocoder that belongs to the class, and to which geocoders sets attributes that tell you about the locaion of a place
# What to test: that it is given the correct domain name...
# However, domain name is not user input...


    def geolocate(self, place): #Find the place, will be used later on, just for syntax simplicity
        time.sleep(self.delay)
        try:
            return self.geocoder.geocode(place,exactly_one=False)[0][1]
        except TypeError:
            print 'Input "%s" not found.' %place
            quit()
# This we can definitely test


    def location_sequence(self, start,end,steps): #Denote the latitude/longitude
        lats = np.linspace(start[0], end[0], steps) # np.linspace returns evenly spaced numbers over an interval
        longs = np.linspace(start[1],end[1], steps)
        return np.vstack([lats, longs]).transpose()
# Returns a matrix of the longitudes and latitudes in a matrix, where they are the columns, not rows
# vstack has the function of stacking the arrays in the rows of a matrix.


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
        if type(green_array)== NoneType:
            raise ValueError('Input location not found')
            quit()

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
