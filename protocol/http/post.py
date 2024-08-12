import requests
import json

def post(method, url, payload):
  headers = {
    'Content-Type': 'application/json',
    'Authorization': '85be84282271fca4af0ae9c7c3ac7023810d2712272686e1eee8f4ce2958b685'
  }

  response = requests.request(method, url, headers=headers, data=payload)
  print(response)
