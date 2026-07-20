import requests
from datetime import datetime

try:
    from zoneinfo import ZoneInfo
except ImportError:
    ZoneInfo = None

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"

def execute(arguments: dict):
    location = (
        arguments.get("city")
        or arguments.get("location")
        or arguments.get("place")
    )

    if location:
        try:
            geo_response = requests.get(
                GEOCODING_URL,
                params={"name": location, "count": 1},
                timeout=10,
            )
            geo_response.raise_for_status()
            geo_data = geo_response.json()

            if "results" not in geo_data or not geo_data["results"]:
                return f"Time Error: location '{location}' not found"

            place_info = geo_data["results"][0]
            timezone_name = place_info.get("timezone")
            city_name = place_info["name"]
            country = place_info.get("country", "")

            if timezone_name and ZoneInfo is not None:
                local_now = datetime.now(ZoneInfo(timezone_name))
                formatted = local_now.strftime("%d-%m-%Y %I:%M:%S %p")
                return (
                    f"{city_name}, {country}: {formatted}"
                    if country
                    else f"{city_name}: {formatted}"
                )

            if timezone_name:
                return f"{city_name}, {country}: timezone {timezone_name}" if country else f"{city_name}: timezone {timezone_name}"

            return f"Time Error: timezone data unavailable for {city_name}"
        except Exception as e:
            return f"Time Error: {e}"

    now = datetime.now()
    return now.strftime("%d-%m-%Y %I:%M:%S %p")


if __name__ == "__main__" :
    print("Time Tool \n")
    print(execute({}))