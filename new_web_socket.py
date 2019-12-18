import websocket
import new_server_pb2
import json
import base64
import sample
import redis_key_value
import time

def on_message(ws, message):
    temp_list=message.split('\n')
    for i in temp_list:
        json_message = json.loads(i)
        payload = base64.b64decode(json_message["Payload"])
        device_id = json_message["Topic"]
        device = new_server_pb2.Device()
        try:
            lis1=device_id.split('/')
            if(lis1[2]=='state'):

                device.ParseFromString(payload)
                if float(device.geoPosition.latitude) > 0.1:
                    print(device_id,device.campaignCode,device.geoPosition.latitude, device.geoPosition.longitude)
                    sample.setfleet(device_id,device.geoPosition.latitude,device.geoPosition.longitude,device.campaignCode)
        except NameError:
            print("Not parseable")

def on_error(ws, error):
    print(error)
def on_close(ws):
    print("### closed ###")
def on_open(ws):
    print("connection establised")
if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://bifrost.adonmo.com:443/ws?access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InRlc3R1c2VyIn0.TtxZ8q90SPr0a47CnynP4bya_8XDkbq3kgRUOqdYvkg&client_type=superuser",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()
