#!/usr/bin/env python3.4
#! python3

# addressIt.py - Reads business names from an excel file.
#			 Returns that business' address
#			 and writes it to the excel file. 

# imports
import openpyxl, webbrowser, sys, pyperclip
from keys import *

#open workbook
print('Opening workbook...')
wb = openpyxl.load_workbook('./Lights out Tracking 2015.xlsx')

#read worksheet
sheet = wb.get_sheet_by_name('Sheet1')

#read business name
businessName = {}
if len(sys.argv) > 1:
	#get busiess name from command line
	business = (sys.argv[1])
	city = (sys.argv[2])

# for row in range(3, get_highest_row + 1):
	# Get the business name from each row of the spreadsheet
	#business = sheet['C' + str(row)].value
	#city = sheet['E' + str(row)].value

#look up place id

#use place id to find address

# return address
webbrowser.open('https://maps.googleapis.com/maps/api/place/textsearch/json?query='+business+' near ' + city + ' illinois&key='+ API_KEY)

# write address to excel file

#webbrowser.open('https://www.google.com/maps/place/' + business + ' ' + city + ' Illinois address')
#	browser.open('https://www.google.com/maps/place/' + address)
# maps.googleapis.com/maps/api/place/textsearch/xml?query
