#!/usr/bin/env python3.4
#! python3

# addressIt.py - Reads business names from an excel file.
#			 Returns that business' address
#			 and writes it to the excel file. 

# imports
import openpyxl, webbrowser, sys, pyperclip, keys

#open workbook
print('Opening workbook...')
wb = openpyxl.load_workbook('./Lights out Tracking 2015.xlsx')

#read worksheet
sheet = wb.get_sheet_by_name('Sheet1')

#read business name
businessName = {}

for row in range(3, get_highest_row + 1):
	# Get the business name from each row of the spreadsheet
	business = sheet['C' + str(row)].value
	city = sheet['E' + str(row)].value

#look up place id

#use place id to find address

# return address
webbrowser.open('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=500&types=food&name=cruise&key=' + API_KEY)

# write address to excel file

webbrowser.open('https://www.google.com/maps/place/' + business + ' ' + city + ' Illinois address')
# page = curl('https://www.google.com/maps/place/' + business + ' ' + city + ' Illinois address')
# print(page)
#	browser.open('https://www.google.com/maps/place/' + address)
# maps.googleapis.com/maps/api/place/textsearch/xml?query
