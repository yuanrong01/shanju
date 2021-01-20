import pytest
from common.Request import *
from common.get_all_data import *
from common.assertResult import *


class TestLogin():
    re = get_data("user", "user")

    @pytest.mark.parametrize("case_id,case_name,url, headers,params, expect_result", re)
    def test_login(self, case_id, case_name, url, headers, params, expect_result):
        log.info("---------------------------开始执行用例---------------------------------")
        log.info("用例编号： {} ,用例名称： {}".format(case_id, case_name))
        result = ReqClient.post(url=url, json=params, headers=headers)
        print(result.text)
        assertResult(result.json(),expect_result)

        log.info("=========================返回参数 ==>> {}".format(result.text))





if __name__ == '__main__':
    pytest.main(['-v','test_user_login.py'])