import time
from random  import randint,choice
import itchat
import pandas as pd

def dealFriendsData(friends):
    '''
    函数的参数是微信好友信息的字典
    微信所有好友的信息抓取
    好友信息中的网名  id  备注   个性签名  城市  性别
    都被保存在了DataFrame数据帧里面  留作备用
    转换好的df被作为返回值返回
    '''
    fs = {}
    for i in friends:
        fs[i['NickName']] = {'UserName':i['UserName'],'Remark':i['RemarkName'],'Sex':i['Sex'],'qianming':i['Signature'],'city':i['City']}
    dfs = pd.DataFrame(fs).T
    return dfs
def initConfig():
    '''
    设置问候语和问候时间段的地方
    words 是问候语设置位置
    time 因为时间是随机的，但是有范围，[7,2]表示<7点之后两小时之内的随机时间>
    
    '''
    config = {'morning':{'flag': True,'words':'早安','time':[7,2]},
              'afternoon':{'flag': True,'words':'晚安','time':[21,2]},
              'daily':{'flag': True,'words':qinghua(),'time':[11,7]}}
    for i,j in config.items():
        config[i]['unix'] = today + j['time'][0]*3600 + randint(1,j['time'][1]*3600)    
    return config
def qinghua():
    '''
    从qinghua.txt中随机取一句话出来
    注意在文本中添加新的情话时候要换行
    
    '''
    with open ('qinghua.txt','r') as file:
        word = file.read()
    word_list = word.split('\n')
    return choice(word_list) 
#登录微信脚本，获取女友的username
itchat.auto_login()
friends = itchat.get_friends(update=True)[1:]
df = dealFriendsData(friends)
she_username = df[df['Remark']=='傻逼兮兮'].iloc[0].UserName

#定时发送信息
today = 1558886400#北京时间2019-05-27 00:00:00 unix时间戳
oneday = 24*60*60
nextday = today + oneday
set_ = initConfig()

while 1:
    now = int(time.time())#获得当前的时间戳
    temp = now - nextday
    #一天过完之后
    if temp > 0:
        today = nextday
        nextday += oneday
        set_ = initConfig()     
    #检测 时间  
    else:
        for i,j in set_.items():
            if now-j['unix'] > 0 and j['flag']:
                itchat.send_msg(j['words'],she_username)
                set_[i]['flag'] = False
    
    
    
        
            
