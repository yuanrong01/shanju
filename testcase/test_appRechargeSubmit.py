from common.assertResult import *
import pytest
from common.get_token import *

class TestRechargeSubmit():
    def setup_class(self):
        self.headers_new = get_token()
    re = get_data("testdata","appRechargeSubmit")


    @pytest.mark.parametrize("case_id,case_name,url, headers,params, expect_result", re)
    def test_appRechargeSubmit(self,case_id, case_name, url, headers, params, expect_result):
        log.info("----------------------------------开始执行用例--------------------------------")
        log.info("用例编号： {} ,用例名称： {}".format(case_id, case_name))
        headers= self.headers_new
        result = ReqClient.post(url=url,json=params,headers=headers)
        assertResult(result.json(), expect_result)
        log.info("==================================返回参数 ==>> {}".format(result.text))

