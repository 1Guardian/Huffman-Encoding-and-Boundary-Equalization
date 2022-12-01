from imports import *

#================================================================
#
# Function: entropy(histogram):
#
# Description: This function takes the histogram and returns entropy
#
# Returns: entropy value
#
#================================================================
def entropy(histogram):
    value = 0.0
    total = 0

    #get cumulative sum from histo
    for j in histogram:
        total += j[1]

    #get the entropy
    for i in histogram:
        value += (i[1]/total) * math.log((i[1]/total), 2.0)

    return -(value)

#================================================================
#
# Function: Lavg(values, histogram):
#
# Description: This function takes the histogram and returns average
#              length of codeword bits
#
# Returns: average Lenght value
#
#================================================================
def Lavg(values, histogram):
    value = 0.0
    total = 0

    #get cumulative sum from histo
    for j in histogram:
        total += j[1]

    #get the actual average
    for key in values:
        for i in histogram:
            if key[0] == i[0].symbol:
                value += (len(key[1]) * (i[1]/total))
                
    return (value)