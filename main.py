import argparse
import logging
import time
import json

from dotenv import load_dotenv

from data.conversion.payload import generate_json as gJSON
from data.sensor.temperature import temp1, temp2
from data.sensor.humidity import hum1, hum2
from data.sensor.powermeter import power
from protocol.http.post import post
# from protocol.mqtt.pub import publish

url = "https://api-dev.bluewave.industries/v1/sensor-data"

def create_payload():
    kWh, kVAR, Hz = power()
    payload = [
        gJSON("03d92a4c-7fd3-45e2-96b0-366269728e1d", temp1()),
        gJSON("9be9e581-edab-4bb9-915b-fe5c87d72021", temp2()),
        gJSON("1a3716c9-1851-4101-ba1c-92ef6559feb2", hum1()),
        gJSON("4cec0158-47a0-4f43-be45-7fcf5c5ff3f6", hum2()),
        gJSON("3cbf56fa-0050-4f4b-8521-21e298807db0", kWh),
        gJSON("ac418648-c692-4201-965d-639a0cdd33bb", kVAR),
        gJSON("227b9cd6-75d8-4fd7-8437-fe6bc27925b0", Hz)
    ]
    return json.dumps({"sensors": payload}, default=str)

def main():
    parser = argparse.ArgumentParser(description='BlueWave SGE')
    parser.add_argument('--interval', type=int, default=60, help='Interval in seconds between each post')
    args = parser.parse_args()
    
    logging.basicConfig(level=logging.INFO)
    
    interval = args.interval
    
    while True:
        payload = create_payload()
        post("POST", url, payload) # use this for HTTP
        # publish("sensor/insert-data", payload) # use this for MQTT
        time.sleep(interval)

if __name__ == '__main__':
    main()
