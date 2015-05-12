#!/usr/bin/env python3.4
#! python3

# mapIt.py - Launches a map in the browser using an address from the 
# command line or clipboard

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
	# Get address from command line.
	business = ' ' .join(sys.argv[1])
	city = ' '.join(sys.argv[2])
else:
	# Get address from clipboard.
	print('Error')

webbrowser.open('https://www.google.com/maps/place' + business + ' in ' + city + ' address')
# webbrowser.open('https://www.google.com/maps/place/' + address)
# maps.googleapis.com/maps/api/place/textsearch/xml?query
