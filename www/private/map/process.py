import json
import os
from pprint import pprint

# def extract_ward(precinct):
#     return precinct.split("-")[0]

# with open("out.json", 'a') as out:
#     with open("franklin-precincts.json", "r") as infile:
#         data = json.loads(infile.read())
#         for feature in data["features"]:
#             feature["properties"]["ward"] = extract_ward(feature["properties"]["PRECINCT"])
#         out.write(json.dumps(data))

with open("ward-coords.json", "r") as f:
    data = json.loads(f.read())
    wards = []
    for feature in data["features"]:
        coords = feature["geometry"]["coordinates"]
        ward = {
            "name": feature["properties"]["ward"],
            "pos": {
                "lat": coords[1],
                "lng": coords[0]
            },
            "current": "",
            "candidates": [{
                    "name": "",
                    "email": "",
                    "phone": "",
                    "stage": "" # interested, pledged, petitioned
                }
            ]
        }
        wards.append(ward);
    wards.sort(key=lambda ward: ward["name"])
    with open("ward-list4.json", "a") as out:
        out.write(json.dumps(wards, indent=5))

