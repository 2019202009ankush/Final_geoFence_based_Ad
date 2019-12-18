import redis_key_value
import time, threading
import sample
import time
WAIT_SECONDS = 5
AlluniqueGeoFence=set()
def runPeriodic():
	print(time.ctime())
	global AlluniqueGeoFence
	AlluniqueGeoFence=redis_key_value.AllSetGeoFenceId()
	for x in AlluniqueGeoFence:
		dic=redis_key_value.getValue(x)
		# print(dic)
		sample.setWebHook(x,dic['circle_x'],dic['circle_y'],dic['radius'])
	threading.Timer(WAIT_SECONDS, runPeriodic).start()
runPeriodic()