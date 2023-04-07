import matplotlib.pyplot as plt 
from matplotlib.ticker import MaxNLocator
import numpy as np
import PIL

# Helper functions for the electron microscope image segmentation project.

def viz(img, is_binary=True, show_pixel_edges=True):
    # Visualize an image. The image is 
    # We have two types of images with different color conventions:
    # - grayscale images: 0 = black, 255 = white, gray values in between
    # - binary images: 0 = white, 1 = black
    # The parameter is_binary specifies what type of image we are dealing with.
    
    # The parameter show_pixel_edges indicates whether or not to draw the pixel edges.
    # Pixel edges are useful on small images like structuring elements, 
    # but clutter images with more rows or columns.
    
    data = np.array(img)
    
    if is_binary:
        cmap = 'gray_r'  # gray reversed
    else:
        cmap = 'gray'
        
    if show_pixel_edges:
        edgecolors = 'r'  # red pixel edges
    else:
        edgecolors = 'none'
        
    plt.figure()
    plt.pcolormesh(data, cmap=cmap, edgecolors=edgecolors, linewidth=1)
    
    ax = plt.gca()
    ax.set_aspect('equal')
    
    # Make y-axis point downward
    ax.invert_yaxis()
    
    # Use integer tick values only
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    
    # IMPROVEME: add a figure size parameter to viz(), or some way to specify the pixel size?
    # IMPROVEME: add optional title?
    # IMPROVEME: center the pixel number labels between the tick, making it easier to see which
    # pixels has which index. Doing so is a bit messy in matplotlib though:
    # see https://matplotlib.org/stable/gallery/ticks/centered_ticklabels.html


# Read an image and return its pixels as a list of lists.
# We assume the image is a grayscale image.
# An image is represented as a list of rows, with each row being a list of pixel intensities.
# The first row in an image is the top-most row, the first pixel in a row is the left-most pixel in a row.
# Usage:
#    img = read_image(filename)
#    val = img[i][j]  # the value of the pixel on row i and column j
#
def read_image(filename):
    image = PIL.Image.open(filename)
    return np.asarray(image).tolist()


# Box filter a binary input image, 
# and return a filtered grayscale image.
# The size of the square filter kernel is 2*half_width+1.
def box_filter_image(img, half_width):
    # The input image img is a binary image
    # (pixel value 0=background=white, 1=object=black)
    
    # Create an empty result image
    height = len(img)
    width = len(img[0])
    result = [[0 for j in range(width)] for i in range(height)]
    
    # Fill in the image
    for i in range(height):
        for j in range(width):
            n = 0  # number of pixels in the average
            acc = 0  # accumulator for the average
            for k in range(-half_width, half_width + 1):
                for l in range(-half_width, half_width + 1):
                    row = i + k
                    col = j + l
                    if col >= 0 and row >= 0 and col < width and row < height:
                        acc = acc + img[row][col]
                        n = n + 1
            # Store the filtered pixel value, but flip its intensity
            # because the output is a grayscale image where 0 is black by convention.
            result[i][j] = 255 - int(255.0 * acc / n)

    return result
