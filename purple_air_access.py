import csv
from datetime import datetime

import purpleair

from config import config

api_read_key = config["purple_air_api_key"]

p = purpleair.PurpleAir(api_read_key)

data = p.get_sensors_data(
    fields=(
        "temperature",
        "humidity",
    ),
    location_type=0,
    modified_since=datetime(year=datetime.now().year, month=datetime.now().month, day=datetime.now().day),
)

with open("purpledata.csv", "w", newline="") as csvfile:
    purpledatawriter = csv.writer(csvfile, delimiter=",", quoting=csv.QUOTE_MINIMAL)
    purpledatawriter.writerow(["PURPLE AIR DATA"])
    purpledatawriter.writerow(["LOCATION", "TEMPERATURE (F)", "HUMIDITY"])

    data_rows = data.get("data")
    for row in data_rows:
        purpledatawriter.writerow(row)
