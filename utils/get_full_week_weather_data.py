import requests
from utils.get_location import get_location
from utils.get_weekend_date import get_weekend_date


def get_full_week_weather_data(start_date, location):
    # calculate the end date
    end_date = get_weekend_date(start_date)

    print(start_date, end_date)

    # get the location's lat and lon
    lat, lon = get_location(location)

    # get the weather data from open-meteo
    response = requests.get(
        f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,rain_sum,wind_speed_10m_max,precipitation_probability_max,relative_humidity_2m_max&start_date={start_date}&end_date={end_date}')
    data = response.json()

    return data
