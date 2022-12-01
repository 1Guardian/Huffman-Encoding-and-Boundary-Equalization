from imports import *

#================================================================
#
# Function: getHisto(image)
#
# Description: This function simply gets a histogram via
#              an image, and puts it into an array and then
#              converts it into a tuple and sorts it
#
# Returns: tuple array sorted in ascending order: (Node(code = intensity, probability = value), count)
#
#================================================================
def getHisto(image):

    #get size of image
    x, y = image.shape[:2]

    #array to store histo values
    histoArray = np.zeros(256)
    sortedHistoValues = []

    #get histogram
    for i in range(x):
        for j in range(y):
            histoArray[image[i][j]] += 1

    #sort the array into a tuple array
    sortedIndices = np.argsort(histoArray)

    for i in sortedIndices:
        if (histoArray[i] > 0):
            sortedHistoValues.append((Nodes(i, histoArray[i]), histoArray[i]))

    return sortedHistoValues