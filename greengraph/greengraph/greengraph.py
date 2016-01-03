#Here we set up the parser

from argparse import ArgumentParser
import map
import numpy as np
from graph import Greengraph
import matplotlib.pyplot as plt
import scipy

# parser
# Need to also add the command to decide the image


if __name__ == "__main__":
    parser = ArgumentParser(description = "Count the green space between two locations")
    parser.add_argument('start', help = 'Input start location')
    parser.add_argument('end', help = 'Input end location')
    parser.add_argument('filename', type=str, help ='image filename with extension')
    parser.add_argument('--steps', type=int, help = 'Number of steps, default = 20')
    parser.add_argument('--plot', '-p', action ='store_true', help ='Display plot')
    #parser.add_argument('--image_type', type=str, help = 'File format of output image')
    arguments = parser.parse_args()

    #img_file = arguments.filename +'.' + arguments.image_type


    mygraph = Greengraph(arguments.start, arguments.end)

    # Set stepsize if entered. Otherwise, set to 20.
    if arguments.steps:
        data = mygraph.green_between(arguments.steps)
    else:
        data = mygraph.green_between(20)

    #Saving and plotting data
    myplot = plt.plot(data)
    #ax = myplot.add_subplot(111)
    #ax.set_title('Greengraph - %s to %s' %(arguments.start, arguments.end))
    plt.savefig(arguments.filename)

    if arguments.plot:
        plt.show()
