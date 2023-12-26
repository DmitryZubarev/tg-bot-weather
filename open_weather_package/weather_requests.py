from .config import weather_token
import requests


def get_weather_json(city_name, weather_token):
    try:
        req = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={weather_token}&units=metric'
        )
        data = req.json()
        return data
    except Exception as ex:
        return None
