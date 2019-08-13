from Tvplay import MovieInfoModel
import re
import requests
class Tvteleplay:
    def __init__(self,data):
        self.__info = MovielnfoModel()
        self.__data_module(data)
    def __data_module(self,data):
        # 获取名称
        pattern = "<span property=\"v:itemreviewed\">(.*)<span class=\"year\">"
        ret = re.search(pattern, data, re.S)
        self.__info.set_name(ret.group(1).split("<")[0])

        # 导演
        pattern = '导演</span>: <span class=\'attrs\'>(.*)<span class=\'pl\'>编剧'
        ret = re.search(pattern, data, re.S)
        pattern = "(.*)</a"
        ret = re.search(pattern, ret.group(1), re.S)
        self.__info.set_dirrector(ret.group().split(">")[1][:-3])

        # 主演
        pattern = '主演</span>(.*)<span class="pl">类型'
        ret = re.search(pattern, data, re.S)
        # ret=ret.group(1)
        str = ""
        for i in ret.group(1).split("</a>")[:-1]:
            i = i.split("\">")[1]
            str += i + "/"
        self.__info.set_author(str)

        # 评分
        pattern = "<div class=\"rating_logo ll\">豆瓣评分</div>(.*)人评价"
        ret = re.search(pattern, data, re.S)
        pattern = "property=\"v:average\">(.*)</strong>"
        ret = re.search(pattern, ret.group(), re.S)
        self.__info.set_actor(ret.group(1))

        # 简介
        pattern = "<div class=\"indent\" id=\"link-report\">(.*)<div id=\"celebrities\" class=\"celebrities related-celebrities\">"
        ret = re.search(pattern, data, re.S)
        pattern = 'class="">(.*)</span>'
        ret = re.search(pattern, ret.group(), re.S)
        self.__info.set_score(ret.group(1))
    @property
    def get(self):
        return self.__info

# # 名称，导演，主演，评分，简介
# ret = requests.get("https://movie.douban.com/subject/26849758/?tag=热门&from=gaia_video")
# data = ret.content.decode("utf-8")
# # print(data)