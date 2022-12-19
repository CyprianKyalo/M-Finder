import requests
import json
import os

def get_ip():
	response = requests.get('https://api64.ipify.org?format=json').json()
	return response['ip']

def get_location():
	ip_addr = get_ip()
	response = requests.get('https://ipapi.co/{}/json/'.format(ip_addr)).json()

	location = {
		"ip": ip_addr,
		"city": response.get("city"),
		"region": response.get("region"),
		"country": response.get("country_name"),
		"latitude": response.get("latitude"),
		'longitude': response.get("longitude")
	}

	return location

	# return list(map(list, location.items()))
