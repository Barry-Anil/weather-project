import requests


api_key = "2db199a15a94910fcfbf391285f1f055"

try:

    base_url = "http://api.openweathermap.org/data/2.5/weather"

    city_name = input("Enter the city name: ")

    params = {"q": city_name, "appid": api_key}
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()

        if "main" in data and "temp" in data["main"]:
            temperature_kelvin = data["main"]["temp"]
            temperature_celsius = temperature_kelvin - 273.15
            print(f"Temperature in {city_name}: {temperature_celsius:.2f}°C")
        else:
            print("Temperature data not found in API response")

    else:
        print("Error in fetching data. Status code:", response.status_code)


