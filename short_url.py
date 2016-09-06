#coding:utf-8
import urllib2
import urllib
import json
from xml import etree


headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0"}
change_site_list = ["http://dwz.cn/create.php"]#baidu

class ChangeUrl(object):
    def __init__(self,long_url=0,short_url=0):
        self.long_url = long_url
        self.short_url = short_url
    @property
    def BaiduLongToShort(self):
        """
        :return: return (long_url,short_url) or (err_msg,error_message)
        """
        data = urllib.urlencode({'url':self.long_url})
        request = urllib2.Request("http://dwz.cn/create.php",data=data,headers=headers)
        response = urllib2.urlopen(request)
        response_dict = json.loads(response.read())
        if response_dict["status"] != 0:
            return  "err_msg",response_dict["err_msg"]
        else:
            return (response_dict["longurl"],response_dict["tinyurl"])

if __name__ == "__main__":
    long_url = "https://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&tn=monline_4_dg&wd=python%20json.loads%20json.load&oq=python%20json.loads&rsv_pq=a2df519f000119a3&rsv_t=617a0si%2FOcFtgG43FVnVfEhmwnXaQbHd4Rg5KuvH5qV2oV%2Fh%2FdvsD5zgP9uQQPpFiNFD&rqlang=cn&rsv_enter=1&inputT=2892&rsv_sug3=15&rsv_sug1=6&rsv_sug7=100&rsv_sug2=0&rsv_sug4=3541"
    change_url = ChangeUrl(long_url)
    long,short =  change_url.BaiduLongToShort
    print long
    print short