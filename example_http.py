import requests
import json

url = "https://api-dev.bluewave.industries/v1/sensor-data"

headers = {
  'Content-Type': 'application/json',
  'Authorization': '85be84282271fca4af0ae9c7c3ac7023810d2712272686e1eee8f4ce2958b685'
}

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

response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)
