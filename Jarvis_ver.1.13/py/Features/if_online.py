from urllib import request
import requests

try:
    requests.post('https://www.google.com/')
    online = True
except:
    online = False