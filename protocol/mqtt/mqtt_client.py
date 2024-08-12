import paho.mqtt.client as mqtt
from dotenv import load_dotenv

mqtt_broker_ip = load_dotenv("MQTT_IP")
mqtt_broker_port = load_dotenv("MQTT_PORT")
mqtt_username = load_dotenv("MQTT_USERNAME")
mqtt_password = load_dotenv("MQTT_PASSWORD")

def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")

mqttClient = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttClient.username_pw_set(mqtt_username, mqtt_password)
mqttClient.on_connect = on_connect

mqttClient.connect(
    host=mqtt_broker_ip,
    port=mqtt_broker_port,
)
