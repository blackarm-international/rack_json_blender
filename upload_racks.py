import json
import requests
import sys

if (len(sys.argv) != 2):
    print("")
    print("this script need to be given the name of the json file as an argument")
    print("")
    exit()

headers = {"Content-Type": "application/json", "Accept": "application/json"}
try:
    with open("config.json", "r") as config:
        credentials = json.load(config)
        user = credentials['USERNAME']
        pwd = credentials['PASSWORD']
        api_url = credentials['APIURL']
except:
    print("unable to load config file")
    exit()
try:
    with open(sys.argv[1], "r") as snow:
        snow_data = json.load(snow)
except:
    print("unable to import upload_racks.json")
    exit()
try:
    for rack_sysid in snow_data:
        data = {}
        data["u_room_name"] = "null"
        data["u_rack_name"] = snow_data[rack_sysid]["u_rack"]
        data["u_rotation"] = snow_data[rack_sysid]["u_rotation"]
        data["u_x_center"] = snow_data[rack_sysid]["u_x_center"]
        data["u_x_size"] = snow_data[rack_sysid]["u_x_size"]
        data["u_y_center"] = snow_data[rack_sysid]["u_y_center"]
        data["u_y_size"] = snow_data[rack_sysid]["u_y_size"]
        data["u_z_center"] = snow_data[rack_sysid]["u_z_center"]
        data["u_z_size"] = snow_data[rack_sysid]["u_z_size"]
        data["u_z_unit_start"] = snow_data[rack_sysid]["u_z_unit_start"]
        response = requests.post(api_url, auth=(user, pwd), headers=headers, json=data)
        print("{} {}".format(snow_data[rack_sysid]["u_rack"], response.status_code))
except:
    print("unable to load snow.json")
    exit()
