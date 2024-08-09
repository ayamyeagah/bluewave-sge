import datetime
import random
import uuid

def generate_json(sensorID, value):
    sensorID = str(sensorID)
    id = uuid.uuid4()

    timestamps = datetime.datetime.now()
    timestamps = timestamps.strftime("%Y-%m-%d %H:%M:%S")

    return {"sensor_id": sensorID, "data": {"id": id, "value": value, "timestamp": timestamps}}
