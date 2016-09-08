#coding:utf-8
import urllib2
import urllib
import json


headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0"}

class ChangeUrl(object):
    """
    Baidu:
        get short url
        also you can use short url to get origin long url
    """
    def __init__(self,long_url=0,short_url=0):
        self.long_url = long_url
        self.short_url = short_url

    def getUrlUseBaidu(self,request):
        response = urllib2.urlopen(request)
        response_dict = json.loads(response.read())
        if response_dict["status"] != 0:
            return "err_msg", response_dict["err_msg"]
        else:
            if response_dict.has_key("tinyurl"):
                return response_dict["tinyurl"]
            else:
                return response_dict["longurl"]

    def baiduUrlLongToShort(self,long_url=0):
        """
        :return: short_url or (err_msg,error_message)
        """
        if long_url:
            self.long_url = long_url
        data = urllib.urlencode({'url': self.long_url})
        request = urllib2.Request("http://dwz.cn/create.php", data=data, headers=headers)
        return self.getUrlUseBaidu(request)

    def baiduUrlShortToLong(self,short_url=0):
        """
        :return: long_url or (err_msg,error_message)
        """
        if short_url:
            self.short_url = short_url
        data = urllib.urlencode({'tinyurl': self.short_url})
        request = urllib2.Request("http://dwz.cn/query.php", data=data, headers=headers)
        return self.getUrlUseBaidu(request)

    def sinaUrlLongToShort(self,long_url=0):
        """
        :return: return short url or None (if Exception)
        """
        if long_url:
            self.long_url = long_url
        # source = ("3213676317", "3271760578")
        try:
            url = "http://api.t.sina.com.cn/short_url/shorten.json?source=3271760578&url_long=" + self.long_url
            request = urllib2.Request(url)
            response = urllib2.urlopen(request,timeout=2)
            response_dict = json.loads(response.read())[0]
            return response_dict["url_short"]
        except Exception as e:
            print e

if __name__ == "__main__":
    change_url = ChangeUrl()
    short_url = change_url.baiduUrlLongToShort("https://www.baidu.com/cache/sethelp/help.html")
    long_url =  change_url.baiduUrlShortToLong("http://dwz.cn/2btGVg")
    print short_url,long_url
    short_url = change_url.sinaUrlLongToShort("https://www.baidu.com/cache/sethelp/help.html")
    print short_url