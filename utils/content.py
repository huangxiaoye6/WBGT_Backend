import requests



def login():
    payload={
        "userId":"xialingdong",
        "password":"13508331699",
    }
    headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
        "host":"app.bjjttec.com",
        "connection":"keep-alive",
        "accept":"application/json, text/plain, */*",
        "accept-encoding":"gzip, deflate, br, zstd"
    }
    res=requests.post(url='https://app.bjjttec.com/auth/login/',json=payload,headers=headers,verify=False)
    content=res.json()
    return content['data']['token']

def get_data(token):
    payload={
        "deviceId":'5cusgf6hikvj',
        "groupId": "",
        "page":1,
        "sort":-1,
    }
    headers={
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
        "token":token,
        "cookie":"sessionid=3mcvc6lqtrmbjscb9ws2zyekr7zwaxna"
    }
    res=requests.post(url="https://app.bjjttec.com/base/history/data/",json=payload,headers=headers,verify=False)
    data=res.json()
    data_list=[]
    for item in data['data']['list']:
        data_dict={
            'createTime':item['createTime'][:-3],
            'WBGTout':item['WBGTout'],
        }
        data_list.append(data_dict)
    content={
        'info':data['data']['list'][0],
        'data_list':data_list,
    }
    return content

def device_status(token):
    payload={

    }
    headers={
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
        "token":token,
        "cookie":"sessionid=3mcvc6lqtrmbjscb9ws2zyekr7zwaxna"
    }
    res=requests.post(url="https://app.bjjttec.com/base/device/list/",json=payload,headers=headers,verify=False)
    data=res.json()
    return data['data']['list'][0]['deviceStatus']
def weather():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',

    }
    params = {
        'key':'750d8c7a74003fef3baf2698ddd0d969',
        'city':'500000',
        'extensions':'base',
        'output':'json',
    }
    res=requests.get(url='https://restapi.amap.com/v3/weather/weatherInfo',headers=headers,params=params)
    content=res.json()
    return content['lives'][0]
if __name__ == '__main__':
    token=login()
    get_data(token)
    device_status(token)
    weather()