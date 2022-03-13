import json
import requests

print(f'Welcome, player!')

#x = requests.get('http://127.0.0.1:8080/')
r = requests.post("http://127.0.0.1:8080/addMoneyTest")