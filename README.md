# Huffman-Encoding-and-Boundary-Equalization
This project implements a very simple compression method for an image, and it extends the tkinter image browser to allow selection of an image region to apply histogram equalization to

## Notes
This project implements an extended version of my tkinter UI to allow a region selection, with histogram equalization being applied in the specified area. The second portion of this project implements a simple huffman encoder via binary trees. Once an image is encoded, the compression ratio is computed, and the entropy estimation vs the actual average is also shown.

## Usage:
Huffman Encoder:
<pre>
python huffman.py -h -t -i imagefile
            -i : image file that you want to work on
            -t : whether or not to generate a thresholded image (8 levels)
            </pre>

<br>
Tkinter Area Selector:
<pre>
python highlight.py -h -t -b -i imagefile
            -i : image file that you want to work on
            -t : whether or not to generate a thresholded image (8 levels)
            -b : whether or not to compress the image using Huffman encoding (this is functionally the same as huffman.py, but it lets you see the thresholded image)
            
