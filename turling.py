'''图灵机器人'''


#coding=utf8
import requests
'''
图灵机器人接口
函数的参数：  微信聊天的时候输入的内容
函数的返回值：图灵机器人的回应
'''
def jqr(info):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : '2a4403884f5f4244ac35396a93d41bba','info'   : info,'userid' : '陈小奇',#
    }
    # 我们通过如下命令发送一个post请求
    r = requests.post(apiUrl, data=data).json()
    # 让我们打印一下返回的值，看一下我们拿到了什么
    print(r)
    try:
        result = r['text']+r['url']
    except KeyError:
        result = r['text']
    try:
        ls = r['list']
        for i in ls[:5]:
            result+=i['article']
            result+='\n'
            result+=i['detailurl']
            result+='\n'
    except KeyError:
        pass
    return result
# print(jqr('qinaide'))