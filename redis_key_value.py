
import redis
import json

r = redis.Redis(host="0.0.0.0",port="6379")

def getValue(geofence_id):
	return json.loads(r.get(geofence_id))
def setValue(geofence_id,name,circle_x,circle_y,radius,isSet,payload,campain_id):
	 r.set(geofence_id,json.dumps({'name':name,'circle_x':circle_x,'circle_y':circle_y,'radius':radius,'isSet':isSet,'payload':payload,'campain_id':campain_id}))
def AllGeoFenceId():
	lis=[k.decode("utf-8") for k  in r.scan_iter("*")]
	return(lis)
def AllSetGeoFenceId():
	lis1=AllGeoFenceId()
	list2 = set()
	for key in lis1:
		if key not in list2:
			dic=getValue(key)
			if dic['isSet']=='T':
				list2.add(key)
	return (list2)
def AllsetGeoFenceIdandCampianPair():
	l=set()
	l=AllSetGeoFenceId()
	lis=[]
	for key in l:
		dic=getValue(key)
		lis.append([key,dic['campain_id']])
	return (lis)
def makeGeoFenInactive(geofence_id):
	dic=getValue(geofence_id)
	dic['isSet']='F'
	r.set(geofence_id,json.dumps(dic))
def makeGeoFenActive(geofence_id):
	dic=getValue(geofence_id)
	dic['isSet']='T'
	r.set(geofence_id,json.dumps(dic))


