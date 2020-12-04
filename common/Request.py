# -*- coding:utf-8 -*-
import requests
from common.Log import *
import json as complexjson
import urllib3


class ReqClient():

    def __init__(self):
        urllib3.disable_warnings()
        self.session = requests.session()

    def get(self,url,**kwargs):
        return self.request(url,"GET",**kwargs)

    def post(self,url,data=None, json=None,**kwargs):

        return self.request(url,"POST",data,json,**kwargs)

    def put(self,url,data=None,**kwargs):
        return self.request(url,"PUT",data,**kwargs)

    def delete(self,url,**kwargs):
        return self.request(url,"DELETE",**kwargs)

    def patch(self,url,data=None,**kwargs):
        return self.request(url,"PATCH",data,**kwargs)

    def request(self,url,method,data=None,json=None,**kwargs):
        url = url
        headers =dict(**kwargs).get("headers")
        params = dict(**kwargs).get("params")
        files = dict(**kwargs).get("files") #需要上传的附件
        cookies = dict(**kwargs).get("cookies")

        try:
            self.requestLog(url, method, data, json, params, headers, files, cookies)
            if method == "GET":
                return self.session.get(url, **kwargs)

            if method == "POST":
                return self.session.post(url, data, json,verify=False, **kwargs)

            if method == "DELETE":
                return self.session.post(url, data, json, **kwargs)

            if method == "PUT":
                if json:
                    # PUT 和 PATCH 中没有提供直接使用json参数的方法，因此需要用data来传入
                    data = complexjson.dumps(json)
                return self.put(url, data, **kwargs)

            if method == "PATCH":
                if json:
                    # PUT 和 PATCH 中没有提供直接使用json参数的方法，因此需要用data来传入
                    data = complexjson.dumps(json)
                return self.put(url, data, **kwargs)
        except Exception as e:
            log.error(e)


    def requestLog(self,url,method,data=None,json=None,params =None,headers=None,files=None,cookies=None,**kwargs):
        log.info("接口请求地址---> {}".format(url))
        log.info("接口请求方式 ---> {}".format(method))
        log.info("接口请求头 ---> {}".format(complexjson.dumps(headers,indent=4,ensure_ascii=False)))
        log.info("接口请求体 data 参数---> {}".format(complexjson.dumps(data,indent=4,ensure_ascii=False)))
        log.info("接口请求体 json 参数---> {}".format(complexjson.dumps(json,indent=4,ensure_ascii=False)))
        log.info("接口请求体 params 参数---> {}".format(complexjson.dumps(params,indent=4,ensure_ascii=False)))
        log.info("接口上传附件 files 参数---> {}".format(files))
        log.info("接口 cookies 参数---> {}".format(complexjson.dumps(cookies, indent=4, ensure_ascii=False)))

ReqClient = ReqClient()
