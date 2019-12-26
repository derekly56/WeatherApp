import requests as re
from geolocation import Geolocation as geo

dark_sky_url = "https://api.darksky.net/forecast/"

SUCCESS = 200
ERROR = 400

class WeatherApp:
	def __init__(self):
		self.url = dark_sky_url
		self.secret_key = "e9892d77feb6377d352f1e92b5dc2c2e"
		self.geolocation = geo()

	def location(self):
		longitude, latitude = self.geolocation.get_location()
		url_full = self.url + self.secret_key + "/" + str(longitude) + "," + str(latitude)

		return url_full

	def get_data(self):
		url_full = self.location()

		req = re.get(url_full)

		if req.status_code == 200:
			weather_data = req.json()
			print(str(weather_data["currently"]["temperature"]) + " F")
		else:
			print("ERROR CODE: " + str(req.status_code))



def main():
	weather = WeatherApp()
	weather.get_data()

if __name__ == "__main__":
	main()
