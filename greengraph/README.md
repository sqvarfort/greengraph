Greengraph 
======================

Authors
--------
Code: James Heatherington
Packaging: Sofia Qvarfort

Description
------------
This is a program that has been packated and distributed as part of the Python Research Programming course. 
Greengraph analyses 20 satellite images between two locations and counts the number of green pixels. 


The output object is a 2D array with the number of steps and corresponding number of green pixels. 


Content
----------
Greengraph contains one constructor (Greengraph) and one object that creates the satellite imagine (Map). 

Greengraph:
Counts the number of green pixels in a Map object

Map:
Fetches a satellite image from Google Maps and turns it into a png image


Sample code
-------------
	
	from numpy import plot as plt
	myplot = Greengraph('London', 'Manchester')
	myplot.plt


Copyright and Licence
-----------------------
For licence and copyright, see LICENCE.md
