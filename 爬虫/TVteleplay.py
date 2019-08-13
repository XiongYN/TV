
# -*- coding:utf-8 -*-
from Tvplay import MovieInfoModel
import re
import requests
class Tvteleplay:
    def __init__(self,data):
        self.__info = MovielnfoModel()
        self.__data_module(data)
    def __data_module(self,data):
        # ��ȡ����
        pattern = "<span property=\"v:itemreviewed\">(.*)<span class=\"year\">"
        ret = re.search(pattern, data, re.S)
        self.__info.set_name(ret.group(1).split("<")[0])

        # ����
        pattern = '����</span>: <span class=\'attrs\'>(.*)<span class=\'pl\'>���'
        ret = re.search(pattern, data, re.S)
        pattern = "(.*)</a"
        ret = re.search(pattern, ret.group(1), re.S)
        self.__info.set_dirrector(ret.group().split(">")[1][:-3])

        # ����
        pattern = '����</span>(.*)<span class="pl">����'
        ret = re.search(pattern, data, re.S)
        # ret=ret.group(1)
        str = ""
        for i in ret.group(1).split("</a>")[:-1]:
            i = i.split("\">")[1]
            str += i + "/"
        self.__info.set_author(str)

        # ����
        pattern = "<div class=\"rating_logo ll\">��������</div>(.*)������"
        ret = re.search(pattern, data, re.S)
        pattern = "property=\"v:average\">(.*)</strong>"
        ret = re.search(pattern, ret.group(), re.S)
        self.__info.set_actor(ret.group(1))

        # ���
        pattern = "<div class=\"indent\" id=\"link-report\">(.*)<div id=\"celebrities\" class=\"celebrities related-celebrities\">"
        ret = re.search(pattern, data, re.S)
        pattern = 'class="">(.*)</span>'
        ret = re.search(pattern, ret.group(), re.S)
        self.__info.set_score(ret.group(1))
    @property
    def get(self):
        return self.__info

# # ���ƣ����ݣ����ݣ����֣����
# ret = requests.get("https://movie.douban.com/subject/26849758/?tag=����&from=gaia_video")
# data = ret.content.decode("utf-8")
# # print(data)
