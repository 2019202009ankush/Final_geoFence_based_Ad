import redis_key_value

print("Enter the details of geofence")
print("Enter the geofence_id")
geofence_id=input()
print("Enter the geofence_name")
name_of_geofence=input()
print("Enter the x coordinate of center")
x_coordinate_of_geofence_center=input()
print("Enter the y coordinate of center")
y_coordinate_of_geofence_center=input()
print("Enter the radius")
radius=input()
print("Enter wether you want to set it")
is_geoFence_set=input()
print("Enter the payload")
payload=input()
print("Enter the campaign_id")
campaign_id=input()

redis_key_value.set_value(geofence_id,name_of_geofence,x_coordinate_of_geofence_center,y_coordinate_of_geofence_center,radius,is_geoFence_set,payload,campaign_id)
redis_key_value.all_set_geo_fence_id()
