#!/usr/bin/env python3.4
#! python3

# placeSearch.py - takes (2) arguments, the business name and the business city
#				   -it returns and object of the first address returned by Google
#				   places search

import json, requests, sys, pprint

def placeFind(business, city, state):
	 
	url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?'
	
	params = dict(
		query = business + ' in ' + city + ' , ' + state,
		key = 'AIzaSyBsWslE0hWtwUrnSGwzKYFXczjmtyuwEwc'
	)	

	data = requests.get(url=url, params=params).json()
	print(data['formatted_address'])

