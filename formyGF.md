# python让你的个人微信号像梦一样自由

#### 起源

笔者是一个coder，

一个有女朋友的coder。

一个有女朋友但特别懒的coder，

一个有女朋友但特别懒可还是很想让女朋友如沐春风的coder，

一个有女朋友但特别懒可还是很想让女朋友如沐春风可记性不大好的coder，





​		后来发现，呆板如笔者，实在难于兼容女朋友大人的需求版本，譬如，每天的早安晚安打卡总是因为一把游戏或者一个需求的影响忘得死死的，当想起来了的时候发现该到下一轮的打卡了。总是因为这样让人难以控制的原因需要解释安抚半天，这让笔者绝望并且懊恼。直到有一天看到这句话，**人工智能可以替代人类从事一部分工作,把人类*从繁杂*、*重复的劳动中解脱出来*,从事更加需要感性思维的工作,如艺术、科研、神学、哲学等工作。**一瞬间醍醐灌顶，繁杂、重复、解脱、解脱，一个可怕但是让笔者兴奋不已的想法开始在脑海中生根发芽。

#### 干

​		有了这个想法之后，笔者就迅速开始准备策划，千万不要等女朋友受不了我之后才做出来呀，眼看他起高楼，眼看他宴宾客，眼看他楼塌了，这是多么绝望的情景呀，毕竟，有女朋友是一件值得让程序员骄傲的事，可是有过女朋友，就要逊色太多了，想到这里，百度已经帮笔者找到了解决方案，itchat，迅速翻文档，测试代码，

[](https://itchat.readthedocs.io/zh/latest/)经过简单的api研究，安装完模块，就开始了第一个版本的开发工作，



1：python 控制微信自动发送消息

```python
import itchat

itchat.auto_login()

itchat.send('Hello, world', toUserName='filehelper')
```

完工运行，文件助手收到了，我的第一条消息，可是来不及兴奋，笔者赶紧进行研究文档，看怎么去给特定好友好友发送信息，**toUserName**应该是每个好友都有的类似网名或者id的东西，想到这里，就决定得先把所有好友的信息拿下来研究一番，

```python
 friends = itchat.get_friends(update=True)[1:]  
```

拿到好友信息，进行简单的数据结构分析，便发现了其中的奥秘

```python
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
```

经过以上操作，好友的信息便被安排的明明白白，通过对信息中的命名的检查，一眼找到 **UserName**的信息，

想要找到女朋友的username手到擒来

```python
she_username = df[df['Remark']=='女朋友的备注'].iloc[0].UserName
```

ok!至此，只剩下时间的问题了，要选在什么时间呢，不能太早，不能太晚，不能天天准点发，一个随机时间还不足以让笔者费脑筋

```python
import time
from random  import randint

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
    
        
            
```

​		定时发送经过unix时间戳的灵活运用，实现了完美随机，接下来就是情话了，笔者是没有说情话的天分的，但是作为一个spider，从来都不怕，笔者准备了一个txt文本，把平常看到的听到的情话整理了起来，随机读取一下试试，

```python
def qinghua():
    '''
    从qinghua.txt中随机取一句话出来
    注意在文本中添加新的情话时候要换行
    
    '''
    with open ('qinghua.txt','r') as file:
        word = file.read()
    word_list = word.split('\n')
    return choice(word_list) 
```

![微信图片_20190527191248](C:\Users\Administrator\Desktop\微信图片_20190527191248.jpg)



