# blender_datacenterVR

## view the original racks
> python3 json_to_obj.py TEST-1-0-2.json > old.obj

import old.obj into blender

## change the rack data and view the new racks
> python3 TEST-1-0-2.py TEST-1-0-2.json > new.json

> python3 json_to_obj.py new.json > new.obj

import old.obj into blender

## rack rotation
0 - facing -Y<br/>
1 - facing +X<br/>
2 - facing +Y<br/>
3 - facing -X<br/>
<br/>
all of the xyz coordinates in the json and servicenow tables are in blender format for ease of use