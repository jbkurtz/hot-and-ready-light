from gpiozero import LED

import os
import sys
import json
import time
import requests

led = LED(18)

try:
    with open(os.path.join(sys.path[0], "config.json"), "r") as f:
        config = json.load(f)
        latitude = config["latitude"]
        longitude = config["longitude"]
        rest = config["rest"]
except:
    raise

req_url = f"https://services.krispykreme.com/api/locationsearchresult/?responseType=Full&search=%7B%22Where%22%3A%7B%22LocationTypes%22%3A%5B%22Store%22%2C%22Commissary%22%2C%22Franchise%22%5D%2C%22OpeningDate%22%3A%7B%22ComparisonType%22%3A0%7D%7D%2C%22Take%22%3A%7B%22Min%22%3A3%2C%22DistanceRadius%22%3A100%7D%2C%22PropertyFilters%22%3A%7B%22Attributes%22%3A%5B%22FoursquareVenueId%22%2C%22OpeningType%22%5D%7D%7D&lat={latitude}&lng={longitude}&_=1517112369718"

while True:
    try:
        resp = requests.get(req_url)
        response = resp.json()[0]['Location']['Hotlight']
    except:
        raise

    if response:
        led.on()
    else:
        led.off()

    time.sleep(rest)
