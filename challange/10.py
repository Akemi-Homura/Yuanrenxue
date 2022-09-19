import requests

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
Cookie: sessionid=ubvf202ld6buu45mccuuc6vef76i2755; Hm_lvt_337e99a01a907a08d00bed4a1a52e35d=1661575412,1662869098,1662911600,1662946334; Hm_lpvt_337e99a01a907a08d00bed4a1a52e35d=1662950132'''
headers = dict((h.partition(':')[0], h.partition(':')[2].strip()) for h in rawheaders.split('\n'))
# headers = {
#     'Host': 'www.python-spider.com',
#     'accept': 'application/json, text/javascript, */*; q=0.01',
#     'accept-language': 'zh-CN,zh;q=0.9',
#     'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
#     'cookie': 'sessionid=ubvf202ld6buu45mccuuc6vef76i2755; Hm_lvt_337e99a01a907a08d00bed4a1a52e35d=1661575412,1662869098,1662911600,1662946334; Hm_lpvt_337e99a01a907a08d00bed4a1a52e35d=1662950132',
#     'origin': 'https://www.python-spider.com',
#     'referer': 'https://www.python-spider.com/challenge/10',
#     'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'same-origin',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'x-requested-with': 'XMLHttpRequest',
# }


# fiddler_proxies = {
#     'http': 'http://127.0.0.1:12345',
#     'https': 'http://127.0.0.1:12345'
# }

session = requests.session()
session.headers = headers

ret = 0

for i in range(1, 101):
    data = {
        'page': i
    }
    response = session.post('https://www.python-spider.com/api/challenge10', data=data)
    if response.status_code != 200:
        raise ValueError
    for item in response.json()['data']:
        ret += int(item['value'])

print(ret)