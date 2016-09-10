#coding:utf-8
try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode
try:
    from urllib.request import Request
    from urllib.request import urlopen
except:
    from urllib2 import Request
    from urllib2 import urlopen
import json


headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0"}

class ChangeUrl(object):
    """
    Baidu Sina:
        get short url or long url
    """
    def __init__(self,long_url=0,short_url=0):
        self.long_url = long_url
        self.short_url = short_url

    def getUrlUseBaidu(self,request):
        try:
            response = urlopen(request,timeout=2)
            response_dict = json.loads(response.read().decode("utf-8"))
            if response_dict["status"] != 0:
                return "err_msg", response_dict["err_msg"]
            else:
                if "tinyurl" in response_dict:
                    return response_dict["tinyurl"]
                else:
                    return response_dict["longurl"]
        except Exception as e:
            print(e)
            return None

    def baiduUrlLongToShort(self,long_url=0):
        """
        :return: return baidu short_url or (err_msg,error_message)
        """
        if long_url:
            self.long_url = long_url
        data = urlencode({'url': self.long_url}).encode("utf-8")
        request = Request("http://dwz.cn/create.php", data=data, headers=headers)
        return self.getUrlUseBaidu(request)

    def baiduUrlShortToLong(self,short_url=0):
        """
        :return: return baidu long_url or (err_msg,error_message)
        """
        if short_url:
            self.short_url = short_url
        data = urlencode({'tinyurl': self.short_url}).encode("utf-8")
        request = Request("http://dwz.cn/query.php", data=data, headers=headers)
        return self.getUrlUseBaidu(request)

    def sinaUrlLongToShort(self,long_url=0):
        """
        :return: return sina short url or None (if try except)
        """
        if long_url:
            self.long_url = long_url
        # source = ("3213676317", "3271760578")
        try:
            url = "http://api.t.sina.com.cn/short_url/shorten.json?source=3271760578&url_long=" + self.long_url
            request = Request(url)
            response = urlopen(request,timeout=2)
            response_dict = json.loads(response.read().decode("utf-8"))[0]
            return response_dict["url_short"]
        except Exception as e:
            print(e)

    def sinaUrlShortToLong(self, short_url=0):
        """
        :return: return sina long url or None (if try except )
        """
        if short_url:
            self.short_url = short_url
        try:
            url = "http://api.t.sina.com.cn/short_url/expand.json?source=3271760578&url_short=" + self.short_url
            request = Request(url)
            response = urlopen(request, timeout=5)
            response_dict = json.loads(response.read().decode("utf-8"))[0]
            return response_dict["url_long"]
        except Exception as e:
            print(e)

if __name__ == "__main__":
    change_url = ChangeUrl()
    baidu_short_url = change_url.baiduUrlLongToShort("https://www.baidu.com/cache/sethelp/help.html")
    baidu_long_url =  change_url.baiduUrlShortToLong("http://dwz.cn/2btGVg")
    print(baidu_short_url,baidu_long_url)
    sina_short_url = change_url.sinaUrlLongToShort("https://www.baidu.com/cache/sethelp/help.html")
    sina_long_url = change_url.sinaUrlShortToLong("http://t.cn/RApcXsB")
    print(sina_short_url,sina_long_url)


