import paho.mqtt.client as mqtt

mqtt_broker_ip = "34.124.239.203"
mqtt_broker_port = 1883
mqtt_username = "bluewave"
mqtt_password = "blu3w4vep455"

def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")

mqttClient = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttClient.username_pw_set(mqtt_username, mqtt_password)
mqttClient.on_connect = on_connect

mqttClient.connect(
    host=mqtt_broker_ip,
    port=mqtt_broker_port,
)
