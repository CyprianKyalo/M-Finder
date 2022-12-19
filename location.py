import requests
import json
import os
import time


def get_ip():
	response = requests.get('https://api64.ipify.org?format=json')

	return response.json()['ip']


def get_location():
	ip_addr = get_ip()

	api_key = os.environ.get("location_api_key")

	# resp = requests.get('https://ipapi.co/{}/json/'.format(ip_addr))
	# resp = requests.get('http://api.ipstack.com/{}'.format(ip_addr))
	resp = requests.get(f'http://api.ipstack.com/{ip_addr}', params={'access_key': api_key})

	# time.sleep(5)

	response = resp.json()

	location = {
		"ip": ip_addr,
		"city": response.get("city"),
		"region": response.get("region_name"),
		"country": response.get("country_name"),
		"latitude": response.get("latitude"),
		'longitude': response.get("longitude")
	}

	return location
