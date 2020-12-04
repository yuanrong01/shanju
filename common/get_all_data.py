import os
from common.readData import *

base_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def get_yaml_data(yaml_file_name):
    yaml_file_path = os.path.join(base_path, "data", yaml_file_name)
    yaml_data = ReadFileData.load_yaml(yaml_file_path)
    return yaml_data

def get_json_data(json_file_name):
    json_file_path = os.path.join(base_path, "data", json_file_name)
    json_data = ReadFileData.load_json(json_file_path)
    return json_data

def get_ini_data(ini_file_name):
    ini_file_path = os.path.join(base_path, "config", ini_file_name)
    ini_data = ReadFileData.load_ini(ini_file_path)
    return ini_data

#获取yaml文件中的数据，并且组合成list的元组数列
def get_data(yaml_file_name,case):
    case_name = []
    headers = []
    case_id = []
    url = []
    params = []
    expect_result = []
    re = get_yaml_data(yaml_file_name)[case]["testcase"]
    for td in re:

        case_name.append(td.get("case_name",{}))
        headers.append(td.get("headers",{}))
        case_id.append(td.get("case_id",{}))
        url.append(td.get("url",{}))
        params.append(td.get("parameter",{}))
        expect_result.append(td.get("expect_result",{}))
    list_params = list(zip(case_id,case_name,url, headers,params, expect_result))
    return list_params