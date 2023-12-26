def parse_weather(json_data):
    if not(json_data is None):
        weather = {
            'city': json_data['name'],
            'temperature': json_data['main']['temp'],
            'humidity': json_data['main']['humidity'],
            'pressure': json_data['main']['pressure'],
            'wind': json_data['wind']['speed']
        }
        return weather
    else:
        return None
