# -*- coding:utf-8 -*-
import logging, time, os
from logging import handlers

log_path = 'D:\project\shanju\Testlog'


class Log:

    def __init__(self):
        #文件命名
        self.logname = os.path.join(log_path,'%s.log' % time.strftime('%Y_%m_%d_%H_%M_%S'))

        #创建logger
        self.logger = logging.getLogger()
        #设置日志等级
        self.logger.setLevel(logging.DEBUG)
        #输出日志格式
        self.formatter = logging.Formatter('[%(asctime)s]-%(filename)s[line:%(lineno)d]-fuc:%(funcName)s-%(levelname)s:%(message)s')

    def __console(self, level, message):
        #创建一个FileHandler,用于写日志到本地（fh = logging.FileHandler(self.logname,'w')）
        fh = logging.FileHandler(self.logname,mode='a', encoding='utf-8')#追加模式
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)

        #给logger添加handler
        self.logger.addHandler(fh)

        #创建一个streamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)
        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        #避免日志输出重复
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        fh.close()

    def debug(self, message):

        self.__console('debug', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):

        self.__console('error', message)

    def info(self, message):

        self.__console('info', message)


log = Log()