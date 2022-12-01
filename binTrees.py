class Nodes:

    #constructor
    def __init__(self, symbol, probability, left = None, right = None):  

        #node pointers
        self.right = right
        self.left = left

        #value of node
        self.symbol = symbol
        self.probability = probability

        #portion of huffman binary represented
        self.code = ''

class BinaryTree:

    #constructor
    def __init__(self, probability, symbol):
        
        #starting node
        self.header = Nodes(probability, symbol)