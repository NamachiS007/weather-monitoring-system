import requests
from config.config import Config

class APIService:
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    @classmethod
    def get_weather(cls, location):
        params = {
            'q': location,
            'appid': Config.OPENWEATHERMAP_API_KEY,
            'units': 'metric'  # Get temperature in Celsius
        }
        response = requests.get(cls.BASE_URL, params=params)
        return response.json()