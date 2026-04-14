import os
import requests


API_KEY = os.environ.get("API_KEY")
if not API_KEY:
    raise SystemExit("API_KEY is required")

URL = "http://api.weatherapi.com/v1/current.json"
params = {"key": API_KEY, "q": "Paris"}

try:
    resp = requests.get(URL, params=params, timeout=10)
    resp.raise_for_status()
except requests.RequestException as e:
    print("Request error", e)
    raise SystemExit(1)

data = resp.json()


def get_weather() -> None:
    local = data.get("location", {})
    current = data.get("current", {})
    print(f"{local['name']}/{local['country']} "
          f"{local['localtime']} "
          f"Weather: {current['temp_c']} Celsius "
          f"{current['condition']['text']}")


if __name__ == "__main__":
    get_weather()
