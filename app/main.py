import os
import requests


API_key = os.environ.get("API_KEY")
if not API_key:
    raise SystemExit("API_KEY is required")
url = f"http://api.weatherapi.com/v1/current.json?key={API_key}&q=Paris"

resp = requests.get(url)
data = resp.json()

def get_weather() -> None:
    print(f"{data['location']['name']}/{data['location']['country']} "
          f"{data['location']['localtime']} "
          f"Weather: {data['current']['temp_c']} Celsius, "
          f"{data['current']['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
