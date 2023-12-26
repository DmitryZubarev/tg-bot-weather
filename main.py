from open_weather_package.config import weather_token
from open_weather_package.weather_requests import get_weather_json
from open_weather_package.parser import parse_weather


def main():
    city = input("Город: ")
    data_json = get_weather_json(city, weather_token)
    data = parse_weather(data_json)
    print(data)


if __name__ == '__main__':
    main()
