import requests as re

dark_sky_url = "https://api.darksky.net/forecast"

SUCCESS = 200
ERROR = 404

class WeatherApp:
	def __init__(self):
		self.url = dark_sky_url
		self.secret_key = "e9892d77feb6377d352f1e92b5dc2c2e"

	def get_location(self):
		raise Exception("Function not yet defined")

	def get(self):
		raise Exception("Function not yet defined")
