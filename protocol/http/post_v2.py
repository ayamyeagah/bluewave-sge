import requests
import json

def post(data1, data2, data3, data4, data5):
  url = "https://api-dev.bluewave.industries/v1/sensor-data"
  headers = {
    'Content-Type': 'application/json',
    'Authorization': '85be84282271fca4af0ae9c7c3ac7023810d2712272686e1eee8f4ce2958b685'
  }
  payload = json.dumps({
    "sensors": [
      data1,
      data2,
      data3,
      data4,
      data5,
    ]
  }, default=str)
  response = requests.request("POST", url, headers=headers, data=payload)
  print(response)

# url = "https://api-dev.bluewave.industries/v1/sensor-data"

# headers = {
#   'Content-Type': 'application/json',
#   'Authorization': '85be84282271fca4af0ae9c7c3ac7023810d2712272686e1eee8f4ce2958b685'
# }

# payload = json.dumps({
#   "sensors": [
#     generate_json("03d92a4c-7fd3-45e2-96b0-366269728e1d", temp1()),
#     generate_json("9be9e581-edab-4bb9-915b-fe5c87d72021", temp2()),
#     generate_json("1a3716c9-1851-4101-ba1c-92ef6559feb2", hum1()),
#     generate_json("4cec0158-47a0-4f43-be45-7fcf5c5ff3f6", hum2()),
#     generate_json("3cbf56fa-0050-4f4b-8521-21e298807db0", power()),
#   ]
# })

# response = requests.request("POST", url, headers=headers, data=payload)
# print(response)
