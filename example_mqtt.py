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
          "value": 77.44,
          "timestamp": "2024-08-09 08:50:00"
        },
        {
          "id": 2,
          "value": 44.5,
          "timestamp": "2024-08-09 08:50:00"
        },
        {
          "id": 3,
          "value": 60.69,
          "timestamp": "2024-08-09 08:50:00"
        }
      ]
    },
    {
      "sensor_id": "b9d5fcbf-99c9-4a01-b7cb-a13aba7b502c",
      "data": [
        {
          "id": 1,
          "value": 77.44,
          "timestamp": "2024-08-09 08:50:00"
        },
        {
          "id": 2,
          "value": 99.5,
          "timestamp": "2024-08-09 08:50:00"
        },
        {
          "id": 3,
          "value": 77.7,
          "timestamp": "2024-08-09 08:50:00"
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
