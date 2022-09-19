import requests

cookies = {
    'sessionid': 'ubvf202ld6buu45mccuuc6vef76i2755',
    'Hm_lvt_337e99a01a907a08d00bed4a1a52e35d': '1661575412,1662869098,1662911600,1662946334',
    'm': '60fce2d174b7b50b7022473baa895d01|1662952381000',
    'Hm_lpvt_337e99a01a907a08d00bed4a1a52e35d': '1662952394',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '0',
    'Origin': 'https://www.python-spider.com',
    'Referer': 'https://www.python-spider.com/challenge/7',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
}

ret = 0

for i in range(1, 101):
    data = {
        'page': i
    }
    if requests.post('https://www.python-spider.com/cityjson', headers=headers, cookies=cookies, data=data).status_code != 200:
        raise ValueError
    response = requests.post('https://www.python-spider.com/api/challenge7', headers=headers, cookies=cookies, data=data)
    if response.status_code != 200:
        raise ValueError
    for item in response.json()['data']:
        ret += int(item['value'])

print(ret)
