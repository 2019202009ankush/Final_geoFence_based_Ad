import redis
import time
from decimal import Decimal
import random
def setWebHook(fence_id,x_coordinate_of_geofence_center,y_coordinate_of_geofence_center,radius):
    client=redis.Redis(host='127.0.0.1', port=9851)
    result=client.execute_command('SETHOOK',fence_id,'mqtt://127.0.0.1:1883/test?qos=2&retained=0','NEARBY','fleet','POINT',x_coordinate_of_geofence_center,y_coordinate_of_geofence_center,radius)
    print('setting setWebHook',result)
def setfleet(deviceId,a,b,c):
    a1=float(a)
    b1=float(b)
    client = redis.Redis(host='127.0.0.1', port=9851)
    result = client.execute_command('SET', 'fleet',deviceId,'FIELD', 'campaignCode',c, 'POINT', a1, b1)
    print (deviceId,a1,b1,c,result)
def delWebHook(fence_id):
    client=redis.Redis(host='127.0.0.1', port=9851)
    result=client.execute_command('DELHOOK',fence_id)
