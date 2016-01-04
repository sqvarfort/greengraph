import numpy as np
import geopy
from map import Map

# This is the constructor
# Should we divide these two into two files? I would
# Create one map object and one greengraph object


# Create the Greengraph object
class Greengraph(object):
    def __init__(self, start, end): #These is the main object that I create with the start and end location
        self.start=start # Declare local variables?
        self.end=end
        self.geocoder=geopy.geocoders.GoogleV3(domain="maps.google.co.uk")  #Create object, geocoder that belongs to the class, and to which geocoders sets attributes that tell you about the locaion of a place
# What to test: that it is given the correct domain name...
# However, domain name is not user input...


    def geolocate(self, place): #Find the place, will be used later on, just for syntax simplicity
        return self.geocoder.geocode(place,exactly_one=False)[0][1]



# This we can definitely test


    def location_sequence(self, start,end,steps): #Denote the latitude/longitude
        lats = np.linspace(start[0], end[0], steps) # np.linspace returns evenly spaced numbers over an interval
        longs = np.linspace(start[1],end[1], steps)
        return np.vstack([lats, longs]).transpose()
# Returns a matrix of the longitudes and latitudes in a matrix, where they are the columns, not rows
# vstack has the function of stacking the arrays in the rows of a matrix.


# This returns an array with two values: the steps and the
    def green_between(self, steps):
        try:
            green_array = [Map(*location).count_green()
            for location in self.location_sequence(
            self.geolocate(self.start),
            self.geolocate(self.end),steps)]
            return green_array
        except:
            print 'Error: Input location not found. ' 
            quit()
        #
