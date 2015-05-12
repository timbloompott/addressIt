#!/usr/bin/env python3.4
#! python3

# mapIt.py - Launches a map in the browser using an address from the 
# command line or clipboard

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
	# Get address from command line.
	business = sys.argv[1]
	city = sys.argv[2]
else:
	# Get address from clipboard.
	print('Error')

webbrowser.open('https://www.google.com/maps/place/' + business + ' ' + city + ' Illinois address')
page = curl('https://www.google.com/maps/place/' + business + ' ' + city + ' Illinois address')
print(page)
#	browser.open('https://www.google.com/maps/place/' + address)
# maps.googleapis.com/maps/api/place/textsearch/xml?query
