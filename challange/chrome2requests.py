rawheaders = '''Host: www.python-spider.com
Connection: keep-alive
Content-Length: 6
sec-ch-ua: "Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"
Accept: application/json, text/javascript, */*; q=0.01
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
sec-ch-ua-mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36
sec-ch-ua-platform: "Windows"
Origin: https://www.python-spider.com
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://www.python-spider.com/challenge/10
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cookie: sessionid=ubvf202ld6buu45mccuuc6vef76i2755; Hm_lvt_337e99a01a907a08d00bed4a1a52e35d=1661575412,1662869098,1662911600,1662946334; Hm_lpvt_337e99a01a907a08d00bed4a1a52e35d=1662950132
'''

dict([[h.partition(':')[0], h.partition(':')[2]] for h in rawheaders.split('\n')])