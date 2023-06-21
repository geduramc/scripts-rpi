import socket
import requests
import json

# pip install requests

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
myip = s.getsockname()[0]
print(myip)


res = requests.get('http://localhost:3000/ping')
response = json.loads(res.text)
print(response)
