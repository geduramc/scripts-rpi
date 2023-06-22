import socket
import requests
import json
import time

# pip install requests
API_URL = 'http://localhost:3000'
API_API_KEY = 'C4A030B5EEEB5EB06C611306DAB237E441A3FACF'
HOST_NAME = 'rpi0'


def get_api_token():
  response = requests.post(f'{API_URL}/api/auth', json = { 
    'name:': HOST_NAME,
    'user': HOST_NAME,
    'key': API_API_KEY
  })
  return json.loads(response.text)

def get_my_ip():
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.connect(("8.8.8.8", 80))
  return s.getsockname()[0]

def send_my_ip():
  token = get_api_token()['data']['token']
  response = requests.post(f'{API_URL}/api/message/t', json = { 
    'sender': HOST_NAME,
    'message': f'myip {get_my_ip()}'
  }, headers = {
    'Authorization': f'Bearer {token}'
  })

flag = 0
while flag == 0:
  try:
    request = requests.get("https://8.8.8.8", timeout=5)
  except (requests.ConnectionError, requests.Timeout):
    print('ERR_INTERNET_DISCONNECTED')
  else:
    send_my_ip()
    flag = 1
  time.sleep(5)