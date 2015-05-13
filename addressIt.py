#!/usr/bin/env python3.4
#! python3

# addressIt.py - Reads business names from an excel file.
#			 Returns that business' address
#			 and writes it to the excel file. 

#open workbook
import openpyxl
wb = openpyxl.load_workbook('./Lights out Tracking 2015.xlsx')
type(wb)

#read worksheet
sheet = wb.get_sheet_by_name('Sheet1')

#read business name

#look up place id

#use place id to find address

# return address

# write address to excel file


import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
	# Get business and city from command line. 
	business = sys.argv[1]
	city = sys.argv[2]
else:
	# Get address from clipboard.
	print('Error')

webbrowser.open('https://www.google.com/maps/place/' + business + ' ' + city + ' Illinois address')
#page = curl('https://www.google.com/maps/place/' + business + ' ' + city + ' Illinois address')
#print(page)
#	browser.open('https://www.google.com/maps/place/' + address)
# maps.googleapis.com/maps/api/place/textsearch/xml?query
