import requests
import json
import time
import os

final_dict = {}

eu_capitals = [
{"city": "Vienna", "country": "Austria", "lat": 48.2082, "lon": 16.3738},
{"city": "Brussels", "country": "Belgium", "lat": 50.8503, "lon": 4.3517},
{"city": "Sofia", "country": "Bulgaria", "lat": 42.6977, "lon": 23.3219},
{"city": "Zagreb", "country": "Croatia", "lat": 45.8150, "lon": 15.9819},
{"city": "Nicosia", "country": "Cyprus", "lat": 35.1856, "lon": 33.3823},
{"city": "Prague", "country": "Czechia", "lat": 50.0755, "lon": 14.4378},
{"city": "Copenhagen", "country": "Denmark", "lat": 55.6761, "lon": 12.5683},
{"city": "Tallinn", "country": "Estonia", "lat": 59.4370, "lon": 24.7536},
{"city": "Helsinki", "country": "Finland", "lat": 60.1695, "lon": 24.9354},
{"city": "Paris", "country": "France", "lat": 48.8566, "lon": 2.3522},
{"city": "Berlin", "country": "Germany", "lat": 52.5200, "lon": 13.4050},
{"city": "Athens", "country": "Greece", "lat": 37.9838, "lon": 23.7275},
{"city": "Budapest", "country": "Hungary", "lat": 47.4979, "lon": 19.0402},
{"city": "Dublin", "country": "Ireland", "lat": 53.3498, "lon": -6.2603},
{"city": "Rome", "country": "Italy", "lat": 41.9028, "lon": 12.4964},
{"city": "Riga", "country": "Latvia", "lat": 56.9496, "lon": 24.1052},
{"city": "Vilnius", "country": "Lithuania", "lat": 54.6872, "lon": 25.2797},
{"city": "Luxembourg", "country": "Luxembourg", "lat": 49.6116, "lon": 6.1319},
{"city": "Valletta", "country": "Malta", "lat": 35.8989, "lon": 14.5146},
{"city": "Amsterdam", "country": "Netherlands", "lat": 52.3676, "lon": 4.9041},
{"city": "Warsaw", "country": "Poland", "lat": 52.2297, "lon": 21.0122},
{"city": "Lisbon", "country": "Portugal", "lat": 38.7223, "lon": -9.1393},
{"city": "Bucharest", "country": "Romania", "lat": 44.4268, "lon": 26.1025},
{"city": "Bratislava", "country": "Slovakia", "lat": 48.1486, "lon": 17.1077},
{"city": "Ljubljana", "country": "Slovenia", "lat": 46.0569, "lon": 14.5058},
{"city": "Madrid", "country": "Spain", "lat": 40.4168, "lon": -3.7038},
{"city": "Stockholm", "country": "Sweden", "lat": 59.3293, "lon": 18.0686}
]


url = "https://api.open-meteo.com/v1/forecast"

for capital in eu_capitals:
    try:
        params = {
            "longitude": capital["lon"],
            "latitude": capital["lat"],
            "current_weather": True,
            "hourly": "temperature_2m,precipitation_probability,weathercode"
        }
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        city_weather_data = response.json()
        capital_final_dict = {}
        capital_final_dict["country"] = capital["country"]
        capital_final_dict["coordinates"] = {"latitude": capital["lat"], "longitude": capital["lon"]}
        capital_final_dict["current_weather"] = city_weather_data["current_weather"]
        hourly_forecast = []
        hour_dict = city_weather_data["hourly"]
        for i in range(len(hour_dict["time"])):
            hourly_entry = {
                "time": hour_dict["time"][i],
                "temperature_2m": hour_dict["temperature_2m"][i],
                "precipitation_probability": hour_dict["precipitation_probability"][i],
                "weathercode": hour_dict["weathercode"][i]
            }
            hourly_forecast.append(hourly_entry)
        capital_final_dict["hourly_forecast"] = hourly_forecast
        final_dict[capital["city"]] = capital_final_dict

        #print(json.dumps(capital_final_dict, indent=4))
        time.sleep(0.75)  # To avoid hitting API rate limits
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON for {capital['city']}: {e}")
    except requests.exceptions.RequestException as e:
        print(f"API request failed for {capital['city']}: {e}")

file_path = os.path.join(os.path.dirname(__file__), "eu_weather_data.json")
with open(file_path, "w") as f:
    f.write(json.dumps(final_dict, indent=3))
