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

    arguments = parser.parse_args()


    mygraph = Greengraph(arguments.start, arguments.end) # Create Greengraph object



    # Set stepsize if entered. Otherwise, set to 20.
    if arguments.steps:
        data = mygraph.green_between(arguments.steps)
    else:
        data = mygraph.green_between(20)

    # Catch API overload error
    # Google sends error picture with 325 green pixels.
    error_threshold = 5
    count = 0
    for iterate in range(0,arguments.steps):
        if data[iterate] == 323:
            count += 1
    if count >= error_threshold:
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
