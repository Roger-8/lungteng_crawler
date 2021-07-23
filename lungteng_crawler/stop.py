#code by fan_31
import requests
from bs4 import BeautifulSoup
import os
import time


#Line Notify封包
headers = {
        "Authorization": "Bearer " + "SQsf4gSmwpI9Z16I08p7hVCKWy1XzLDxB1RXgF27WrG",
        "Content-Type": "application/x-www-form-urlencoded"
    }

#Line Notify發送通知
params = {"message": "\n server stoped!!" + "\n restarting~~"}

#/////////////////////////////////////////////////////////////////////////////////////////////////

r = requests.post("https://notify-api.line.me/api/notify",
                      headers=headers, params=params)
print(r.status_code)  #200
