import requests
from twilio.rest import Client

OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "908911b0e7304483f411be45eefd"
account_sid = "AC3430fa41d35fcb069f77f7953"
auth_token = "b5295c0d5f15ce8a6ef1257f60"

weather_params = {
    "lat": 45.657974,
    "lon": 25.601198,
    "appid": api_key,
    "cnt": 4,
}
response = requests.get(OWM_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Bring your umbrella",
        from_="+16592011727",
        to='+216 21 045 283'
    )

    print(message.status)
