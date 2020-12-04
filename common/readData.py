import yaml
from common.Log import *
import json
from configparser import ConfigParser

class MyConfigParser(ConfigParser):
    # 重写 configparser 中的 optionxform 函数，解决 .ini 文件中的 键option 自动转为小写的问题
    def __init__(self, defaults=None):
        ConfigParser.__init__(self, defaults=defaults)

    def optionxform(self, optionstr):
        return optionstr

class ReadFileData():

    def __init__(self):
        pass

    def load_yaml(self,file_path):

        log.info("加载 {} 文件...".format(file_path))
        with open(file_path,encoding='utf-8') as f:
            data = yaml.safe_load(f)
        log.info("读取到数据---> {} ".format(data))
        return data

    def load_json(self,file_path):
        log.info("加载 {} 文件...".format(file_path))
        with open(file_path,encoding='utf-8') as f:
            data = json.load(f)
        log.info("读取到数据---> {} ".format(data))
        return data

    def load_ini(self,file_path):
        log.info("加载 {} 文件...".format(file_path))
        config = MyConfigParser()
        config.read(file_path,encoding='utf-8')
        data = dict(config._sections)
        log.info("读取到数据---> {} ".format(data))
        return data



ReadFileData = ReadFileData()

