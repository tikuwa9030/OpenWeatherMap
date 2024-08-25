import requests


def get_weather(city_name, api_key):
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    PARAMS = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }

    response = requests.get(BASE_URL, params=PARAMS)

    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]

        print(f"City: {city_name}")
        print(f"Temperatures: {main['temp']}")
        print(f"Weather: {weather['description']}")
    else:
        print(f"エラー： {response.status_code}")
        print(f"Error: {response.text}")


api_key = '442b068094f88bad3f4c0ac7edae1def'
city_name = 'Tokyo'
get_weather(city_name, api_key)
