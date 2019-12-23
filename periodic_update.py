import redis_key_value
import time, threading
import sample
import time
WAIT_SECONDS = 5
all_unique_geo_fence=set()

def runPeriodic():
	global all_unique_geo_fence
	all_unique_geo_fence=redis_key_value.all_set_geo_fence_id()
	print("Running a periodic_update ",flush=True)
	for x in all_unique_geo_fence:
		dic=redis_key_value.get_value(x)
		sample.set_web_hook(x,dic['x_coordinate_of_geofence_center'],dic['y_coordinate_of_geofence_center'],dic['radius'])
	threading.Timer(WAIT_SECONDS, runPeriodic).start()

runPeriodic()
