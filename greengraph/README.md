Greengraph
======================

Authors
--------
Code: James Heatherington
Packaging: Sofia Qvarfort

Description
------------
This is a program that has been packaged and distributed as part of the Python Research Programming course given at UCL 2015-2016.
Greengraph analyses 20 satellite images between two locations and counts the number of green pixels.

The output object is a list with the number of steps and corresponding number of green pixels.

Usage
------
Run greengraph.py from the command line. The program takes the following arguments:

	start 		The start location
	end		The final location
	--plot, -p	Show plot of graph
	--steps, -s 	Change the step size, or number of satellite images
	--delay, -d	Input delay in seconds before each request



Sample usage
-------------
From the command line, input

	>> python greengraph.py London Manchester -p -s 30 -d 1


Warnings end Errors
----------------------
Google API overload: The Google Map API only accepts a limited number of requests within 24 hours or within a short time span. 
Repeated use of greengraph.py can hit the upper limit of requests, which results in a flat line graph with a constant pixel count of 323, because the Api sends an error image with this number of green pixels.
The program prints a warning when the API limit has been reached. 

Bad input: Bad input, such as an unknown start or end location, negative step or delay, or an invalid image file extension will result in an error. 


Copyright and Licence
-----------------------
For licence and copyright, see LICENCE.md
