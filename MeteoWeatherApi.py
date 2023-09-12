import schedule
import time
import requests


def getWeather(lat, long):
    baseUrl = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&hourly=temperature_2m"
    response = requests.get(baseUrl)
    data = response.json()
    return data

def CtF(celcius):
    return (celcius * 9 / 5) * 32

def todaysWeather():
    lat = 35.04596
    long = -85.0529

    weatherData = getWeather(lat, long)
    temperatureC = getWeather["hourly"]["temperature_2m"][0]
    relativeHumidity = getWeather["hourly"]["relativehumidity_2m"][0]
    windSpeed = getWeather["hourly"]["windspeed_10m"][0]
    temperatureF = CtF(temperatureC)

    weather = (
        f"Good morning!\n"
        f"Current weather at Hickman Science Center:\n"
        f"Temperature: {temperatureF}"
        f"Humidity: {relativeHumidity}"
        f"Wind Speed: {windSpeed}"
    )

    return weather
