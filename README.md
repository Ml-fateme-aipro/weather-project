# Weather Project

A simple Python app that shows current weather (temperature, humidity,
wind speed, conditions) for any city, using the OpenWeatherMap API.

## Features
- Search weather by city name
- Handles invalid city names and API errors
- API key stored safely in a .env file (never committed)

## Tech
Python, requests, python-dotenv

## Setup
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file with: `API_KEY=your_openweathermap_key`
4. Run: `python weather.py`
