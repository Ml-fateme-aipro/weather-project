import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def get_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(url, params=params)
    if response.status_code != 200:
        return None
    return response.json()


def main():
    city = input("اسم شهر (انگلیسی): ")
    data = get_weather(city)

    if data is None:
        print("شهر پیدا نشد یا مشکلی در API هست.")
        return

    print("شهر:", data["name"])
    print("وضعیت:", data["weather"][0]["description"])
    print("دما:", data["main"]["temp"], "°C")
    print("رطوبت:", data["main"]["humidity"], "%")
    print("سرعت باد:", data["wind"]["speed"], "m/s")


if __name__ == "__main__":
    main()