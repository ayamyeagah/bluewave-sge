import argparse
import logging
import time
import json
import os
from dotenv import load_dotenv

from data.conversion.payload import generate_json as gJSON
from data.sensor.THD import S71200
from data.sensor.powermeter import power
# from protocol.http.post import post
from protocol.mqtt.pub import MQTT

load_dotenv()

# env variables
URL = os.getenv('URL')
MQTT_IP = os.getenv('MQTT_IP')
MQTT_PORT = os.getenv('MQTT_PORT')
MQTT_USERNAME = os.getenv('MQTT_USERNAME')
MQTT_PASSWORD = os.getenv('MQTT_PASSWORD')
PLC_IP = os.getenv('PLC_IP')
DB_NUM = 1
START = 0
SIZE = 16

p_mqtt = MQTT(MQTT_USERNAME, MQTT_PASSWORD)
p_mqtt.connect(MQTT_IP, MQTT_PORT)

plc = S71200(PLC_IP)
plc.connect()

data = plc.read(DB_NUM, START, SIZE)

def c_payload():
    if data:
        temp1, temp2, hum1, hum2 = data
        print(temp1, temp2, hum1, hum2)
    else: 
        temp1 = temp2 = hum1 = hum2 = None
        print("No data available")

    kWh, kVAR, Hz = power()
    payload = [
        gJSON("03d92a4c-7fd3-45e2-96b0-366269728e1d", temp1),
        gJSON("9be9e581-edab-4bb9-915b-fe5c87d72021", temp2),
        gJSON("1a3716c9-1851-4101-ba1c-92ef6559feb2", hum1),
        gJSON("4cec0158-47a0-4f43-be45-7fcf5c5ff3f6", hum2),
        gJSON("3cbf56fa-0050-4f4b-8521-21e298807db0", kWh),
        gJSON("ac418648-c692-4201-965d-639a0cdd33bb", kVAR),
        gJSON("227b9cd6-75d8-4fd7-8437-fe6bc27925b0", Hz)
    ]
    return json.dumps({"sensors": payload}, default=str)

def main():
    parser = argparse.ArgumentParser(description='Bluewave SGE')
    parser.add_argument('--interval', type=int, default=60)
    args = parser.parse_args()
    
    logging.basicConfig(level=logging.INFO)
    
    interval = args.interval
    
    while True:
        payload = c_payload()
        # post("POST", URL, payload) # use this for HTTP
        p_mqtt.publish("sensor/insert-data", payload) # use this for MQTT
        time.sleep(interval)

if __name__ == '__main__':
    main()
