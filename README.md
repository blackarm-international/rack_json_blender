# blender_datacenterVR

## change with code
* download the obj file from datacenterVR
* convert to a json file with convert_blender_obj_to_json.py
> python3 convert_blender_obj_to_json.py example.obj > example.json
* modify the rack sizes, positions and rotation with modify.py
> python3 modify.py example.json > final.json
* upload the racks to servicenow with upload_racks.py
> python3 upload_racks.py final.json

## rack rotation
0 - facing -Y<br/>
1 - facing +X<br/>
2 - facing +Y<br/>
3 - facing -X<br/>
<br/>
all of the xyz coordinates in the json and servicenow tables are in blender format for ease of use