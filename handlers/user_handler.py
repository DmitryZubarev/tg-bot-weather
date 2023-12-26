from aiogram.types import Message
from aiogram import Router
from open_weather_package.weather_requests import get_weather_json
from open_weather_package.parser import parse_weather


router = Router()

# ---------------------- Command handlers ----------------------

@router.message()
async def process_message(message: Message):
    city_name = message.text
    weather_json = get_weather_json(city_name, 'e0f76067109250c530e2448bcc013f31')
    weather = parse_weather(weather_json)
    weather_string = f"city - {weather['city']}, \n" \
                     f"temperature - {weather['temperature']}, \n" \
                     f"humidity - {weather['humidity']}, \n" \
                     f"pressure - {weather['pressure']}, \n" \
                     f"wind_speed - {weather['wind']} \n"
    await message.answer(text=weather_string)
