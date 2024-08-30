import argparse
import logging
import time
import json
import os
from dotenv import load_dotenv

from data.conversion.payload import generate_json as gJSON
from data.sensor.THD import S71200
from data.sensor.powermeter import PM
# from protocol.http.post import post
from protocol.mqtt.pub import MQTTc as MQTT

load_dotenv()

# env variables
URL = os.getenv('URL')
MQTT_IP = os.getenv('MQTT_IP')
MQTT_PORT = os.getenv('MQTT_PORT')
MQTT_USERNAME = os.getenv('MQTT_USERNAME')
MQTT_PASSWORD = os.getenv('MQTT_PASSWORD')
SERIAL_PORT = os.getenv('SERIAL_PORT')
PLC_IP = os.getenv('PLC_IP')
DB_NUM = 1
START = 16
SIZE = 16

p_mqtt = MQTT(MQTT_USERNAME, MQTT_PASSWORD)
plc = S71200(PLC_IP)
pm = PM(SERIAL_PORT, 9600)

p_mqtt.connect(MQTT_IP, MQTT_PORT)
plc.connect()
pm.connect()

def c_payload():
    data = plc.read(DB_NUM, START, SIZE)

    if data:
        temp1, temp2, hum1, hum2 = data
        print(temp1, temp2, hum1, hum2)
    else: 
        temp1 = temp2 = hum1 = hum2 = None
        print("No data available")

    registers = [56, 58, 62]
    rBuffer = []
    for reg in registers:
        rBuffer.append(pm.read(reg, 2))
    Hz, kVARh, kWh = rBuffer
    print(kWh, kVARh, Hz)
    
    payload = [
        gJSON(os.gotenv('SENSOR_ID_TEMP1'), temp1),
        gJSON(os.gotenv('SENSOR_ID_TEMP2'), temp2),
        gJSON(os.gotenv('SENSOR_ID_HUM1'), hum1),
        gJSON(os.gotenv('SENSOR_ID_HUM2'), hum2),
        gJSON(os.gotenv('SENSOR_ID_KWH'), kWh),
        gJSON(os.gotenv('SENSOR_ID_KVARH'), kVARh),
        gJSON(os.gotenv('SENSOR_ID_HZ'), Hz)
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
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        plc.disconnect()
        pm.disconnect()
        p_mqtt.disconnect()
        logging.info('Exiting...')
        exit
