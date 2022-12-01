from imports import *
from getHistogram import *
from AverageCalcs import *
finalKeys = []

#================================================================
#
# Function: findKeyInTree(Tree, key, value)
#
# Description: This function is probably the laziest bit of code
#              I have ever slapped my name onto. IT just walks
#              through the tree until it finds a key and returns
#              that key's value via the global array I stored
#              at the start of the file
#
# Returns: tuple array sorted in ascending order: (Node(code = intensity, probability = value), count)
#
#================================================================
def findKeyInTree(Tree, key, value):

        temp_key_l = key
        temp_key_r = key

        #go right
        if Tree.symbol == -1:
            
            temp_key_l += "0"
            temp_key_r += "1"

            findKeyInTree(Tree.right, temp_key_r, value)
            findKeyInTree(Tree.left, temp_key_l, value)

        elif Tree.symbol != -1:
            global finalKeys
            finalKeys.append((Tree.symbol, key))

        else:
            return

#================================================================
#
# Function: compressionRatio(histogram, x, y):
#
# Description: This function takes the histogram and the image size
#              to calculate how much compression we actually achieved
#
# Returns: void
#
#================================================================
def compressionRatio(histogram, x, y):
    
    #get finalKeys
    global finalKeys;

    #get total number of bits used to store the original image
    before_compression = x * y * 8

    #convert to dict for parsing
    finalKeysDict = dict(finalKeys)

    #get the number of bits that would be used with new encoding
    after_compression = 0
    for symbol in histogram:
        count = symbol[1]
        after_compression += count * len(finalKeysDict[symbol[0].symbol]) 

    #print
    print("Space usage before compression (in bits):", before_compression)    
    print("Space usage after compression (in bits):",  after_compression)      

    #account for bad compressions
    print("Compression Ratio: ", str('%.3f'%(before_compression/after_compression)) + ":1")     

    #print average bpp length estimate
    print("Shannon Theorem/Entropy Average Length: ", entropy(histogram), "bpp")

    #print real average bpp length
    print("Huffman Encoding Average Length: ", Lavg(finalKeys,  histogram), "bpp")

#================================================================
#
# Function: createHuffLUT(image)
#
# Description: This function takes the histogram we got from the
#              previous function and creates a huffman tree out
#              of the values. It then converts it into a LUT 
#              for ease of encoding
#
# Returns: Huffman Tree formed by the histogram values and the 
#          LUT formed from the table
#
#================================================================

def createHuffLUT(image):

    #get the histo and remove first element
    #and generate first node
    sortedHistoValues = getHisto(image)

    #extract smallest elements and form tree until we are out of elements
    while len(sortedHistoValues) > 1:

        firstNode = sortedHistoValues.pop(0)
        secondNode = sortedHistoValues.pop(0)

        #make new node 
        newNode = Nodes(-1, (firstNode[0].probability + secondNode[0].probability), firstNode[0], secondNode[0])
       
        #put back in queue and resort them
        sortedHistoValues.append((newNode, newNode.probability))
        sortedHistoValues.sort(key=lambda y: y[1])

    #now make a LUT using our Tree
    Tree = sortedHistoValues[0][0]
    
    sortedHistoValues = getHisto(image)

    findKeyInTree(Tree, "", 1)

    #print compression ratio
    print(finalKeys)
    print("====================================================================================")
    compressionRatio(getHisto(image), image.shape[0], image.shape[1])
    print("====================================================================================")

    #return our tree and LUT
    return (Tree, finalKeys)