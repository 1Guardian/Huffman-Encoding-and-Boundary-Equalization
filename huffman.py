#==============================================================================
#
# Class : CS 5420
#
# Author : Tyler Martin
#
# Project Name : Project 6 | Huffman Encoding (Standalone)
#
# Date: 11-21-2022
#
# Description: This is just a segment of the project which only does the 
#              compression calculations related to the huffman encoding
#
# Notes: Since I know you prefer to read and work in C++, this file is set
#        up to mimic a standard C/C++ flow style, including a __main__()
#        declaration for ease of viewing. Also, while semi-colons are not 
#        required in python, they can be placed at the end of lines anyway, 
#        usually to denote a specific thing. In my case, they denote globals, 
#        and global access, just to once again make it easier to parse my code
#        and see what it is doing and accessing.
#
#==============================================================================

#"header" file imports
from imports import *
from checkImages import *
from getMetaData import *
from grayScaleImage import *
from HuffmanEncoding import *
from restrictIntensities import *

#================================================================
#
# GLOBALS
#
#================================================================
currentImg = 0;
maxSize = 0;
currentImage = 0;
originalName = "out";
originalImage = 0;
boxIdentifier = None
boxCorners = []
globalpath = "/"
x = 1080;
y = 720;

#================================================================
#
# Function: __main__
#
# Description: This function is the python equivalent to a main
#              function in C/C++ (added just for ease of your
#              reading, it has no practical purpose)
#
#================================================================

def __main__(argv):

    #gain access to our globals
    global maxSize;
    global currentImg;
    global currentImage;
    global originalImage;
    global originalName;
    global globalpath;
    global x;
    global y;

    #variable to hold path
    path = "nothing"
    thresh = False
    Huffman = True

    # get arguments and parse
    try:
      opts, args = getopt.getopt(argv,"tbh:i:")
    except getopt.GetoptError:
        print("huffman.py -h -t -i imagefile")
        print("===========================================================================================================")
        print("-i : image file that you want to work on")
        print("-t : whether or not to generate a thresholded image (8 levels)")
        sys.exit(2)
    for opt, arg in opts:
        if opt == ("-h"):
            print("huffman.py -h -t -i imagefile")
            print("===========================================================================================================")
            print("-i : image file that you want to work on")
            print("-t : whether or not to generate a thresholded image (8 levels)")
            sys.exit(2)
        elif opt in ("-i", "--img"):
            path = arg
        elif opt in ("-t", "--thresh"):
            thresh = True

    #make sure we got at the least, a path
    if (path == "nothing"):
        print("you must provide an image to start with!")
        sys.exit(2)

    #set max size global
    originalImage = grayScaleImage(checkImages(path))
    currentImage = originalImage

    #check and see if we are supposed to restrict the intensities
    if thresh:
        currentImage = restrictIntensities(currentImage)

    #set the window size
    globalpath = path
    originalName = os.path.splitext(os.path.basename(path))[0]
    meta = getMetaData(currentImage)
    x = meta.get("sizeX")
    y = meta.get("sizeY")

    #check huffman
    if Huffman:
        print("Original Intensity : Huffman Code") 
        print("====================================================================================")
        createHuffLUT(originalImage)

#start main
argv = ""
__main__(sys.argv[1:])