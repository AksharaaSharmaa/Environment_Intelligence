from fastapi import FastAPI
import requests
import os

app = FastAPI()

WAQI_TOKEN = os.getenv("WAQI_TOKEN")

@app.post("/environment-intelligence")
def environment_intelligence(data: dict):

    city = data.get("city")
    country = data.get("country")
    latitude = data.get("latitude")
    longitude = data.get("longitude")

    results = {}

    weather = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": latitude,
            "longitude": longitude,
            "current_weather": True
        }
    ).json()

    results["weather"] = weather

    aqi = requests.get(
        f"https://api.waqi.info/feed/{city}/",
        params={"token": WAQI_TOKEN}
    ).json()

    results["air_quality"] = aqi

    country_info = requests.get(
        f"https://restcountries.com/v3.1/name/{country}"
    ).json()

    results["country"] = country_info

    return results
