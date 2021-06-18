import json
import sys

if (len(sys.argv) != 2):
    print("")
    print("this script need to be given the name of the json file as an argument")
    print("")
    exit()

try:
    with open(sys.argv[1], "r") as snow:
        snow_data = json.load(snow)
except:
    print("unable to import json")
    exit()

output = []
for rack in snow_data:
    # extract original data
    u_rack_name = rack["u_rack_name"]
    u_room_name = rack["u_room_name"]
    u_rotation = rack["u_rotation"]
    u_x_center = rack["u_x_center"]
    u_x_size = rack["u_x_size"]
    u_y_center = rack["u_y_center"]
    u_y_size = rack["u_z_center"]
    u_z_center = rack["u_z_center"]
    u_z_size = rack["u_z_size"]
    u_z_unit_start = rack["u_z_unit_start"]
    # customize the data
    rack_number = int(u_rack_name[6:8])
    if (rack["u_rack_name"].startswith('TEST-A')):
        u_x_center = 2
        u_rotation = 3
    if (rack["u_rack_name"].startswith('TEST-B')):
        u_x_center = 6
        u_rotation = 1
    if (rack["u_rack_name"].startswith('TEST-C')):
        u_x_center = 10
        u_rotation = 3
    u_x_size = 2
    u_y_center = 2 + rack_number
    u_y_size = 1
    u_z_center = 1.5
    u_z_size = 3
    u_z_unit_start = 0.05
    # store modified data
    output.append({
        "u_room_name": u_room_name,
        "u_rack_name": u_rack_name,
        "u_rotation": u_rotation,
        "u_x_center": u_x_center,
        "u_x_size": u_x_size,
        "u_y_center": u_y_center,
        "u_y_size": u_y_size,
        "u_z_center": u_z_center,
        "u_z_size": u_z_size,
        "u_z_unit_start": u_z_unit_start
    })
print(json.dumps(output, indent=4, sort_keys=True))