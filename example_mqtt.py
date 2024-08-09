import json
import time
from mqtt_client import mqttClient

payload = json.dumps({
  "sensors": [
    {
      "sensor_id": "a189a16a-db33-4760-bec8-b928f953df3a",
      "data": [
        {
          "id": 1,
          "value": 70.43,
          "timestamp": "2024-05-06 09:56:46"
        },
        {
          "id": 2,
          "value": 16.5,
          "timestamp": "2024-05-06 09:56:46"
        },
        {
          "id": 3,
          "value": 64.68,
          "timestamp": "2024-05-06 09:56:46"
        }
      ]
    },
    {
      "sensor_id": "b9d5fcbf-99c9-4a01-b7cb-a13aba7b502c",
      "data": [
        {
          "id": 1,
          "value": 70.43,
          "timestamp": "2024-05-06 09:56:46"
        },
        {
          "id": 2,
          "value": 16.5,
          "timestamp": "2024-05-06 09:56:46"
        },
        {
          "id": 3,
          "value": 64.68,
          "timestamp": "2024-05-06 09:56:46"
        }
      ]
    },
  ]
})


mqttClient.loop_start()

mqtt_topic = "sensor/insert-data"
mqttClient.publish(mqtt_topic, payload=payload)

# Wait for 3 seconds before stopping the loop
time.sleep(3)
mqttClient.loop_stop()
mqttClient.disconnect()
