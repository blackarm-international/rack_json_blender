# blender_datacenterVR

## view the original racks
> python3 json_to_obj.py rack_data.json > old.obj

import old.obj into blender

## change the rack data and view the new racks
> python3 modify_racks.py rack_data.json > new.json

> python3 json_to_obj.py new.json > new.obj

import old.obj into blender

## rack rotation
0 is facing -Y<br/>
1 is facing +X<br/>
2 is facing +Y<br/>
3 is facing -X<br/>
