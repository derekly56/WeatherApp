from geopy.geocoders import Nominatim

class Geolocation:
	def __init__(self):
		self.geolocation = Nominatim(user_agent='WeatherApp')

	def get_location(self):
		loc = input("What location? ")
		location = self.geolocation.geocode(loc)
		longitude,latitude = location.longitude, location.latitude

		return longitude, latitude
