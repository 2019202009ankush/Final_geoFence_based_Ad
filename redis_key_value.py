
import redis
import json
from loading_environment import REDIS_HOST,REDIS_PORT
r = redis.Redis(host=REDIS_HOST,port=REDIS_PORT)

def getValue(geofence_id):
	return json.loads(r.get(geofence_id))
def setValue(geofence_id,name_of_geofence,x_coordinate_of_geofence_center,y_coordinate_of_geofence_center,radius,is_geoFence_set,payload,campaign_id):
	 r.set(geofence_id,json.dumps({'name_of_geofence':name_of_geofence,'x_coordinate_of_geofence_center':x_coordinate_of_geofence_center,'y_coordinate_of_geofence_center':y_coordinate_of_geofence_center,'radius':radius,'is_geoFence_set':is_geoFence_set,'payload':payload,'campaign_id':campaign_id}))
def AllGeoFenceId():
	lis=[k.decode("utf-8") for k  in r.scan_iter("*")]
	return(lis)
def AllSetGeoFenceId():
	lis1=AllGeoFenceId()
	list2 = set()
	for key in lis1:
		if key not in list2:
			dic=getValue(key)
			if dic['is_geoFence_set']=='T':
				list2.add(key)
	return (list2)

def AllsetGeoFenceIdandCampianPair():
	l=set()
	l=AllSetGeoFenceId()
	lis=[]
	for key in l:
		dic=getValue(key)
		lis.append([key,dic['campaign_id']])
	return (lis)
	
def makeGeoFenInactive(geofence_id):
	dic=getValue(geofence_id)
	dic['is_geoFence_set']='F'
	r.set(geofence_id,json.dumps(dic))
def makeGeoFenActive(geofence_id):
	dic=getValue(geofence_id)
	dic['is_geoFence_set']='T'
	r.set(geofence_id,json.dumps(dic))


