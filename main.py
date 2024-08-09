import argparse
import logging

from data.conversion.payload import generate_json as gJSON
from data.sensor.temperature import temp1, temp2
from data.sensor.humidity import hum1, hum2
from data.sensor.powermeter import power
from protocol.http.post_v2 import post

def main():
    parser = argparse.ArgumentParser(description='BlueWave SGE')
    
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO)
    
    post(
        gJSON("03d92a4c-7fd3-45e2-96b0-366269728e1d", temp1()),
        gJSON("9be9e581-edab-4bb9-915b-fe5c87d72021", temp2()),
        gJSON("1a3716c9-1851-4101-ba1c-92ef6559feb2", hum1()),
        gJSON("4cec0158-47a0-4f43-be45-7fcf5c5ff3f6", hum2()),
        gJSON("3cbf56fa-0050-4f4b-8521-21e298807db0", power())
    )

if __name__ == '__main__':
    main()
