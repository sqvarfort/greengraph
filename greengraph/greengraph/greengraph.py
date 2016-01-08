## Greengraph
#----------------------------
# Description:

from argparse import ArgumentParser
import map
import numpy as np
from graph import Greengraph
import matplotlib.pyplot as plt

# Create parser arguments
if __name__ == "__main__":
    parser = ArgumentParser(description = "Count the green space between two locations")
    parser.add_argument('start', help = 'Input start location')
    parser.add_argument('end', help = 'Input end location')
    parser.add_argument('filename', type=str, help ='image filename with extension')
    parser.add_argument('--steps', '-s', type=int, help = 'Number of steps, default = 20')
    parser.add_argument('--plot', '-p', action ='store_true', help ='Display plot')
    parser.add_argument('--delay', '-d', type=int, help = 'API request delay in seconds')

    arguments = parser.parse_args()



    mygraph = Greengraph(arguments.start, arguments.end, arguments.delay) # Create Greengraph object
    data = mygraph.green_between(arguments.steps)

    # Catch API overload error
    # Google sends error picture with 325 green pixels.
    # This method should be in one of the classes
    if mygraph.api_overload(arguments.steps):
        print 'Warning: API overload'


    # Saving and plotting data
    fig = plt.figure()
    plt.plot(data)
    fig.suptitle('Greengraph - %s to %s' %(arguments.start, arguments.end), fontsize=14, fontweight='bold')
    ax = fig.add_subplot(111)
    ax.set_xlabel('steps')
    ax.set_ylabel('green pixel count')
    plt.savefig(arguments.filename) # Save plot

    if arguments.plot: # Show plot if arguments.plot = TRUE
        plt.show()
