from geopy.geocoders import Nominatim

class Geolocation:
	def __init__(self):
		self.geolocation = Nominatim(user_agent='WeatherApp')

	def get_location(self):
		raise Exception("Function not yet defined")
