import json
import traceback
import paho.mqtt.client as mqtt
import redis_key_value
import base64
import asyncio

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("test")

async def sendMessage(message):
    uri = "wss://bifrost.adonmo.com:443/ws?access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InRlc3R1c2VyIn0.TtxZ8q90SPr0a47CnynP4bya_8XDkbq3kgRUOqdYvkg&client_type=superuser"
    import websockets
    async with websockets.connect(uri) as websocket:
        await websocket.send(message)

unique_devices_that_are_inside = set()

def on_message(client, userdata, msg):
    v=msg.payload.decode()
    jmsg = json.loads(v)
    campaignCode = jmsg["fields"]["campaignCode"]
    device_id = jmsg["id"].split('/')[1]
    detect=jmsg["detect"]
    geofence_id=jmsg["hook"]
    coordinate=jmsg["object"]["coordinates"]
    x_coordinate=coordinate[0]
    y_coordinate=coordinate[1]
    
    if detect=='inside':
        if device_id not in unique_devices_that_are_inside:
            unique_devices_that_are_inside.add(device_id)
            print(' [+] {} unique_devices_that_are_inside so far: {}'.format(len(unique_devices_that_are_inside), unique_devices_that_are_inside))
            print(device_id, geofence_id,detect,x_coordinate,y_coordinate,campaignCode)
            # if campaignCode == 711:
            #     print("--- Sending ---", flush=True)
            #     try:
            #         payload_dict = {"1066":{"slides":[{"type":"abhibus_score_slide","data":{"match":{"batting_team_name":"IND*","batting_team_overs":"(15.4)","bowling_team_name":"WI","batting_team_score":"178/2","bowling_team_score":"Yet to bat"}}}],"valid_till_millis":1577840461,"min_supported_version_code":32,"max_supported_version_code":80}}
            #         message1=json.dumps({
            #                     "Topic": "device/" + device_id + "/device-manager/dynamicdataupdate",
            #                     "Payload": base64.b64encode(json.dumps(payload_dict).encode()).decode()
            #                    })
            #         print(device_id,campaignCode,json.dumps(payload_dict, indent=2))
            #         print(message1)
            #         print()
            #         asyncio.get_event_loop().run_until_complete(sendMessage(message1))
            #         print("sent")
            #     except Exception as e:
            #         traceback.print_exc()
            from periodic_update import AlluniqueGeoFence
            print ("hi",AlluniqueGeoFence)
            if geofence_id in AlluniqueGeoFence:
                dic=redis_key_value.getValue(geofence_id)
                if campaignCode!=dic["campaign_id"]:
                    print ('HiiiiiiiiiiisendMessage;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;')               

    else:
        if device_id in unique_devices_that_are_inside:
            unique_devices_that_are_inside.remove(device_id)
            print(' [-] {} unique_devices_that_are_inside so far: {}'.format(len(unique_devices_that_are_inside), unique_devices_that_are_inside))
            print(device_id, campaign_id,detect,x_coordinate,y_coordinate)

client = mqtt.Client()
client.connect("127.0.0.1",1883,60)
client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
