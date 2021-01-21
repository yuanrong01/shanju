from common.Request import *
from common.get_all_data import *


def julogin():

    #获取用户登录信息
    data = get_json_data("admin.json")
    expect_result = data["expect_result"]
    header = {"content-type":"application/json",
              "version":"1.3.0",
              "device": "ios",
              "device-id": "yuanrong-001",
              "device-model": "iphone12",
              "device-os-ver": "13.4.1",
              "token":"${token}"
    }
    url = "http://10.113.248.196/api-user/v1/user/login/phone"
    result = ReqClient.post(url=url,json=data["body"],headers=header)
    assert result.json()["result"]["userId"] == expect_result
    log.info("测试用例通过,返回参数 ==>> {}".format(result.text))
    return result.json()
