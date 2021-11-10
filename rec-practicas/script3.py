import json


def read_json():
    f = open("rec-practicas/myfile.json")

    data = json.load(f)

    print("Name: "+data["value"][1]["name"])
    print("State: "+data["value"][1]["properties"]["provisioningState"])
    print("IP version: "+data["value"][1]["properties"]["publicIPAddressVersion"])
    print("IP: "+data["value"][1]["properties"]["ipAddress"])
    print("Location: "+data["value"][1]["location"])


read_json()
