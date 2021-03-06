# -*- coding: utf-8 -*-
import logging
import os
from logging.handlers import TimedRotatingFileHandler
from tornado.options import define, options
import time

#创建log目录
def mkdir(path):
    # 引入模块

    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        print path+' create success'
        # 创建目录操作函数
        os.makedirs(path)
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print path+' is exist'
        return False

#计算路径，然后创建文件夹
logsPath = os.path.join(options.base_dirname,'logs')
mkdir(logsPath)

#设置logger模块
log = logging.getLogger('mylogger')
if options.env == 'Debug':
    log.setLevel(logging.DEBUG)
else:
    log.setLevel(logging.INFO)

#定义格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#定义文件名
loggerFileName = options.base_dirname+os.sep+'logs'+os.sep+options.logger_name

if options.sep_logger:
    #定义根据日期分割日志
    fileTimeHandler = TimedRotatingFileHandler(loggerFileName, "h", 1, 30)
    fileTimeHandler.suffix = "%Y%m%d"
    fileTimeHandler.setFormatter(formatter)
    log.addHandler(fileTimeHandler)
else:
    #不根据日期分割日志
    fh = logging.FileHandler(loggerFileName)
    fh.setFormatter(formatter)
    log.addHandler(fh)




log.info('log start in {0}'.format(options.env))
