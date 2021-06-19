import json

if (len(sys.argv) != 2):
    print("")
    print("this script needs the name of the json file")
    print("")
    exit()

try:
    with open(sys.argv[1], "r") as snow:
        snow_data = json.load(snow)
except:
    print("unable to import json")
    exit()

output = {}
for rack_sys_id in snow_data:
    # extract original data
    u_rack = snow_data[rack_sys_id]["u_rack"]
    u_rotation = snow_data[rack_sys_id]["u_rotation"]
    u_x_center = snow_data[rack_sys_id]["u_x_center"]
    u_x_size = snow_data[rack_sys_id]["u_x_size"]
    u_y_center = snow_data[rack_sys_id]["u_y_center"]
    u_y_size = snow_data[rack_sys_id]["u_y_size"]
    u_z_center = snow_data[rack_sys_id]["u_z_center"]
    u_z_size = snow_data[rack_sys_id]["u_z_size"]
    u_z_unit_start = snow_data[rack_sys_id]["u_z_unit_start"]
    # customize the data
    rack_number = int(u_rack[15:17])
    if (u_rack.startswith('TEST-1-0-2-0-AG')):
        u_rotation = 1
        u_x_center = 2
        u_x_size = 2
        u_y_center = 20 - rack_number
        u_y_size = 1
        u_z_center = 1.5
        u_z_size = 3
        u_z_unit_start = 0.05
    if (u_rack.startswith('TEST-1-0-2-0-AJ')):
        u_rotation = 3
        u_x_center = 8
        u_x_size = 2
        u_y_center = 20 - rack_number
        u_y_size = 1
        u_z_center = 1.5
        u_z_size = 3
        u_z_unit_start = 0.05
    if (u_rack.startswith('TEST-1-0-2-1-AG')):
        u_rotation = 1
        u_x_center = 2
        u_x_size = 2
        u_y_center = 20 - rack_number
        u_y_size = 1
        u_z_center = 7
        u_z_size = 3
        u_z_unit_start = 0.05
    if (u_rack.startswith('TEST-1-0-2-1-AJ')):
        u_rotation = 3
        u_x_center = 8
        u_x_size = 2
        u_y_center = 20 - rack_number
        u_y_size = 1
        u_z_center = 7
        u_z_size = 3
        u_z_unit_start = 0.05
    # store modified data
    output[rack_sys_id] = {
        "u_rack": u_rack,
        "u_rotation": u_rotation,
        "u_x_center": u_x_center,
        "u_x_size": u_x_size,
        "u_y_center": u_y_center,
        "u_y_size": u_y_size,
        "u_z_center": u_z_center,
        "u_z_size": u_z_size,
        "u_z_unit_start": u_z_unit_start
    }
print(json.dumps(output, indent=4, sort_keys=True))