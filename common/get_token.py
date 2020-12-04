from common.julogin import *
headers={"content-type": "application/json","token":"${token}","version":"1.3.0","device": "ios","device-id": "yuanrong-001","device-model": "iphone12","device-os-ver": "13.4.1"}
real_token = julogin()['result']


def get_token():
   headers["token"] = real_token["token"]
   return headers

