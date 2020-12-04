from common.Log import *
import traceback

def assertResult(real_data,expect_result):

    code = expect_result["code"]
    msg = expect_result["msg"]
    #result = expect_result["result"]
    real_code = real_data["code"]
    real_msg = real_data["msg"]
    #real_result = real_data["result"]

    assert code == real_code
    assert msg == real_msg
    #assert result == real_result

    traceback.print_exc(file=open(log.logname, mode='a', encoding='utf-8'))



