# Data Loader

Python utility to extract metadata from OpenSlide images and post them to a RESTful interface

Installation:
* Tested on python 3.5.0.
* `pip install -r requirements.txt`

Make sure you have `LD_LIBRARY_PATH` set up 

Usage:
`python dataLoader.py -i <inputCSVFile> -o <RESTinterface> -a <API key>`


Issues:
`ImportError: libopenjp2.so.7: cannot open shared object file.`
Run 
`export LD_LIBRARY_PATH=/usr/local/lib`


