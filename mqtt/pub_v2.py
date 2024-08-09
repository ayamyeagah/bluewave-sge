import json
import time
from mqtt_client import mqttClient
from data.payload import generate_json
from data.temperature import temp1, temp2
from data.humidity import hum1, hum2
from data.powermeter import power

payload = json.dumps({
  "sensors": [
    generate_json("03d92a4c-7fd3-45e2-96b0-366269728e1d", temp1()),
    generate_json("9be9e581-edab-4bb9-915b-fe5c87d72021", temp2()),
    generate_json("1a3716c9-1851-4101-ba1c-92ef6559feb2", hum1()),
    generate_json("4cec0158-47a0-4f43-be45-7fcf5c5ff3f6", hum2()),
    generate_json("3cbf56fa-0050-4f4b-8521-21e298807db0", power()),
  ]
})

mqttClient.loop_start()

mqtt_topic = "sensor/insert-data"
mqttClient.publish(mqtt_topic, payload=payload)

# Wait for 3 seconds before stopping the loop
time.sleep(3)
mqttClient.loop_stop()
mqttClient.disconnect()
