import time
from mqtt_client import mqttClient

def publish(mqtt_topic, payload):
  mqttClient.loop_start()
  mqttClient.publish(mqtt_topic, payload=payload)
  time.sleep(3)
  mqttClient.loop_stop()
  mqttClient.disconnect()
