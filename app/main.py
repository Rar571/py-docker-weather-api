import os
import requests


API_KEY = os.environ.get("API_KEY")
if not API_KEY:
    raise SystemExit("API_KEY is required")

CITY = "Paris"
URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    params = {"key": API_KEY, "q": CITY}
    try:
        resp = requests.get(URL, params=params, timeout=10)
        resp.raise_for_status()
    except requests.RequestException as e:
        print("Request error", e)
        raise SystemExit(1)

    data = resp.json()
    loc = data.get("location", {})
    cur = data.get("current", {})
    print(f"{loc.get('name')}/{loc.get('country')} {loc.get('localtime')} "
          f"Weather: {cur.get('temp_c')}°C, {cur.get('condition', {}).get('text')}")


if __name__ == "__main__":
    get_weather()
