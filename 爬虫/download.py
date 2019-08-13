#下载模块

import requests
import threading #导入线程



#数据分析类的父类
class RequestDelegate:

    #接收函数
    def receive_data(self,data):
        pass

#数据下载类，下载了数据发给数据分析类
class Request(threading.Thread):
    def __init__(self,delegate:RequestDelegate):
        #self.__delegate = delegate  #记录接收数据的对象
        super().__init__()
        self.__delegate = delegate
        self.__url = None

    #多线程中的启动多线程的函数
    def request(self,url):
        self.__url = url
        self.start()

    def run(self):
        ret = requests.get(self.__url)
        #得到数据data
        data = ret.content.decode("utf-8")

        #回传对象
        self.__delegate.receive_data(data)

