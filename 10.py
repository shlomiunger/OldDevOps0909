from datetime import datetime
from time import sleep
import requests
print(datetime.now()) #print time

for i in range(5):
    response = requests.get("https://github.com")
    if response.status_code == 200:
        print("github is up and running")
    sleep(5)
print("resolved")

a = 3