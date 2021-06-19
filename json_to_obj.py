#!/usr/bin/python3.6
# use x forward, y up when importing/exporting with blender
import json
import sys

if (len(sys.argv) != 2):
    print("")
    print("this script needs the name of the json file")
    print("")
    print("python3 convert_rack_json_to_blender_obj.py input.json")
    print("")
    exit()

with open(sys.argv[1], 'r', encoding='utf-8') as json_data:
    snow_data = json.loads(json_data.read())
    vert=0
    text=0
    face=0
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
        x_min = u_x_center - (u_x_size / 2)
        x_max = u_x_center + (u_x_size / 2)
        y_min = u_y_center - (u_y_size / 2)
        y_max = u_y_center + (u_y_size / 2)
        z_min = u_z_center - (u_z_size / 2)
        z_max = u_z_center + (u_z_size / 2)
        print("o {}".format(u_rack))
        # v 0.000000 4.000000 -2.000000
        # v 0.000000 5.000000 -2.000000
        # v 0.000000 4.000000 -3.000000
        # v 0.000000 5.000000 -3.000000
        # v 1.000000 4.000000 -2.000000
        # v 1.000000 5.000000 -2.000000
        # v 1.000000 4.000000 -3.000000
        # v 1.000000 5.000000 -3.000000
        print("v {} {} {}".format(x_min, z_min, y_min * -1))
        print("v {} {} {}".format(x_min, z_max, y_min * -1))
        print("v {} {} {}".format(x_min, z_min, y_max * -1))
        print("v {} {} {}".format(x_min, z_max, y_max * -1))
        print("v {} {} {}".format(x_max, z_min, y_min * -1))
        print("v {} {} {}".format(x_max, z_max, y_min * -1))
        print("v {} {} {}".format(x_max, z_min, y_max * -1))
        print("v {} {} {}".format(x_max, z_max, y_max * -1))
        print("vt 0.375000 0.000000")
        print("vt 0.625000 0.000000")
        print("vt 0.625000 0.250000")
        print("vt 0.375000 0.250000")
        print("vt 0.625000 0.500000")
        print("vt 0.375000 0.500000")
        print("vt 0.625000 0.750000")
        print("vt 0.375000 0.750000")
        print("vt 0.625000 1.000000")
        print("vt 0.375000 1.000000")
        print("vt 0.125000 0.500000")
        print("vt 0.125000 0.750000")
        print("vt 0.875000 0.500000")
        print("vt 0.875000 0.750000")
        print("vn -1.0000 0.0000 0.0000")
        print("vn 0.0000 0.0000 -1.0000")
        print("vn 1.0000 0.0000 0.0000")
        print("vn 0.0000 0.0000 1.0000")
        print("vn 0.0000 -1.0000 0.0000")
        print("vn 0.0000 1.0000 0.0000")
        print("usemtl None")
        print("s off")
        #f 1/1/1 2/2/1 4/3/1 3/4/1
        print("f ", end="")
        print("{}/{}/{} ".format((vert + 1), (text + 1), (face + 1)), end="")
        print("{}/{}/{} ".format((vert + 2), (text + 2), (face + 1)), end="")
        print("{}/{}/{} ".format((vert + 4), (text + 3), (face + 1)), end="")
        print("{}/{}/{}".format((vert + 3), (text + 4), (face + 1)))
        #f 3/4/2 4/3/2 8/5/2 7/6/2
        print("f ", end="")
        print("{}/{}/{} ".format((vert + 3), (text + 4), (face + 2)), end="")
        print("{}/{}/{} ".format((vert + 4), (text + 3), (face + 2)), end="")
        print("{}/{}/{} ".format((vert + 8), (text + 5), (face + 2)), end="")
        print("{}/{}/{}".format((vert + 7), (text + 6), (face + 2)))
        #f 7/6/3 8/5/3 6/7/3 5/8/3
        print("f ", end="")
        print("{}/{}/{} ".format((vert + 7), (text + 6), (face + 3)), end="")
        print("{}/{}/{} ".format((vert + 8), (text + 5), (face + 3)), end="")
        print("{}/{}/{} ".format((vert + 6), (text + 7), (face + 3)), end="")
        print("{}/{}/{}".format((vert + 5), (text + 8), (face + 3)))
        #f 5/8/4 6/7/4 2/9/4 1/10/4
        print("f ", end="")
        print("{}/{}/{} ".format((vert + 5), (text + 8), (face + 4)), end="")
        print("{}/{}/{} ".format((vert + 6), (text + 7), (face + 4)), end="")
        print("{}/{}/{} ".format((vert + 2), (text + 9), (face + 4)), end="")
        print("{}/{}/{}".format((vert + 1), (text + 10), (face + 4)))
        #f 3/11/5 7/6/5 5/8/5 1/12/5
        print("f ", end="")
        print("{}/{}/{} ".format((vert + 3), (text + 11), (face + 5)), end="")
        print("{}/{}/{} ".format((vert + 7), (text + 6), (face + 5)), end="")
        print("{}/{}/{} ".format((vert + 5), (text + 8), (face + 5)), end="")
        print("{}/{}/{}".format((vert + 1), (text + 12), (face + 5)))
        #f 8/5/6 4/13/6 2/14/6 6/7/6
        print("f ", end="")
        print("{}/{}/{} ".format((vert + 8), (text + 5), (face + 6)), end="")
        print("{}/{}/{} ".format((vert + 4), (text + 13), (face + 6)), end="")
        print("{}/{}/{} ".format((vert + 2), (text + 14), (face + 6)), end="")
        print("{}/{}/{}".format((vert + 6), (text + 7), (face + 6)))
        print("")
        vert = vert + 8
        text = text + 14
        face = face + 6

        