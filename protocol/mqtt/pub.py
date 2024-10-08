import time
import paho.mqtt.client as mqtt

class MQTTc:
    def __init__(self, username, password):
        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
        self.client.username_pw_set(username, password)
        self.client.on_connect = self.on_connect

    def on_connect(self, client, userdata, flags, reason_code, properties):
        print(f"Connected with result code {reason_code}")
    
    def on_disconnect(self, client, userdata, reason_code):
        print(f"Disconnected with result code {reason_code}")

    def connect(self, ip, port):
        self.client.connect(
            host=ip,
            port=port,
        )

    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()

    def publish(self, mqtt_topic, payload):
        self.client.loop_start()
        self.client.publish(mqtt_topic, payload=payload)
