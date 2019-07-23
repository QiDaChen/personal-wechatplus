import requests
import re
import pickle
import json

def getCityTable(acity,dcity):
    with open("./data/cityjson",'rb') as file:
        cityDict = pickle.load(file)
    try:
        a = cityDict[acity]
        d = cityDict[dcity]
        return [a,d]
    except:
        return False

def getaddr(words):
    adcity = False
    try :
        acity,dcity = re.findall("(.+)到(.+)",words)[0]
        print(acity,dcity)
    except:
        return adcity
    else:
        adcity = getCityTable(acity,dcity)
    finally:
        return adcity
def getlowerprice(resultcity):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
    payload2 = {"flightWay": "Oneway", "dcity": resultcity[0], "acity": resultcity[1]}
    url2 = 'https://flights.ctrip.com/itinerary/api/12808/lowestPrice'
    resultjson = requests.post(url2, json=payload2, headers=headers)
    if resultjson.ok:
        jsons = json.loads(resultjson.text)
        print(jsons)
        if jsons['msg'] == 'success':
            res_list = jsons["data"]['oneWayPrice']
            res_msg = '\n'.join(["时间{}:价格{}".format(k,v) for k,v in res_list[0].items()])
            return res_msg
        else:
            return "这两地间您确定有航班？"
    else:
        return '网络环境差，获取失败'
def getLowerAir(words):
    resultcity = getaddr(words)
    if resultcity:
        return getlowerprice(resultcity)
    else:
        return "您输入的城市太凶了，我都没有找到~"

