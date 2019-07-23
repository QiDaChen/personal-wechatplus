import time
import re
from selenium import webdriver
from PIL import Image
import requests
from lxml import etree
import json
import os
import pickle
import pandas as pd
from Find import *
from turling import *
import itchat
from Find import *
from ctrip import *
message = readsth()
fsflag = {}
msg_to_u = ['你好呀！现在开启微信机器人啦\n你可以获取数据','正在进入网页\n你可能需要根据图片输入验证码','正在获取cookies请稍等',' 已成功获取到cookies，\n接下来我要把所有的数据进行抓取','数据已经被我们完美的爬取下来\n接下来我们可以对数据进行一个查看或者操作\n今日课程计划\n某某同学的课堂反馈\n备课表的在线生成','\n  今日热点','  今日热点\n','     早安\n','    晚安','很抱歉，未找到任何关于这个学生的历史课堂，请检查学生姓名是否输入错误']
driver = ''
pic_xpth = '//*[@id="teacher_form"]/div[2]/div/img'
us_xpath = '//*[@id="teacher_form"]/div[2]/input[1]'
ps_xpath = '//*[@id="teacher_form"]/div[2]/input[3]'
yzm_xpath = '//*[@id="teacher_form"]/div[2]/input[4]'
dl_xpath = '//*[@id="teacher_form"]/input[2]'

def initset(friends):
    global fsflag
    dealData(friends)
    for i in friends:
        fsflag[i['UserName']] = {'tuling':False,'duniang':False}
    return fsflag
def getnews():
    '''
    获取IT之家的热点新闻

    :return: 24h热点文章   168h热点文章
    '''
    import requests
    from lxml import etree
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
    url  = 'https://www.ithome.com/'
    page = requests.get(url,headers=headers)
    page.encoding = 'utf-8'
    tree = etree.HTML(page.text)
    result = '\n the hot news for 24h \n\n'
    week = '\n the top news for 168h \n\n'
    for i in range(12):
        try:
            a = tree.xpath('//*[@id="con"]/div[4]/div[2]/div[3]/div[3]/div[1]/ul/li[{}]/a//text()'.format(i+1))[0]
            b = tree.xpath('//*[@id="con"]/div[4]/div[2]/div[3]/div[3]/div[1]/ul/li[{}]/a/@href'.format(i+1))[0]
            c = tree.xpath('//*[@id="con"]/div[4]/div[2]/div[3]/div[3]/div[2]/ul/li[{}]/a//text()'.format(i+1))[0]
            d = tree.xpath('//*[@id="con"]/div[4]/div[2]/div[3]/div[3]/div[2]/ul/li[{}]/a/@href'.format(i+1))[0]
            week+='{}\n{}\n-------------------------\n'.format(c,d)
            result+='{}\n{}\n-------------------------\n'.format(a,b)
        except:
            break
    return result,week
def getimg(img_time):
    '''得到网页登陆时候所需的验证码图片
       driver是全局变量  后面需要通过driver会的cookies
       成功过得到会返回True
    '''
    global driver
    driver = webdriver.Chrome()
    #driver.set_window_size() # 设置浏览器尺寸
    driver.maximize_window()
    driver.get('https://all-dream.com/front_login.jsp?param=teacher')
    time.sleep(5) # 要加载一段时间，留出时间
    if driver.title == '傲梦直播':
        driver.save_screenshot('.\image\{}.png'.format(img_time))
        yzm_elmt = driver.find_element_by_xpath(pic_xpth)
        L = yzm_elmt.location['x']
        T = yzm_elmt.location['y']
        R = L+yzm_elmt.size['width']
        B = T+yzm_elmt.size['height']
        im = Image.open('.\image\{}.png'.format(img_time))
        print(L,T,R,B)
        im = im.crop((L,T,R,B))
        im.save('.\image\{}1.png'.format(img_time))
        time.sleep(1)
        print(L,T,R,B)
        return True
    else:
        return False

def dealData(friends):
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
    save(dfs)
def save(dfs):
    '''存储所有好友信息到本地'''
    with open('./data/好友信息','wb',) as file2:
        pickle.dump(dfs,file2)
def log_web(ad,yzm):
    '''登陆我们的傲梦网站
       参数是网站登陆所需的验证码
       返回值是网页的driver
    '''
    driver.find_element_by_xpath(us_xpath).send_keys(ad[0])
    driver.find_element_by_xpath(ps_xpath).send_keys(ad[1])
    driver.find_element_by_xpath(yzm_xpath).send_keys(yzm)
    driver.find_element_by_xpath(dl_xpath).click()
    time.sleep(3)
    if driver.title == '老师个人中心':
        print('网页成功登录')
        cook = driver.get_cookies()
        print(cook)
        return True,cwck(cook)
    else:
        print('网页登录失败请检查验证码是否识别正确 ')
        return False,0
def cwck(cook):
    '''转换cookies成为爬虫所需的格式
       列表转换为字典
    '''
    cookies = {}
    for i in cook:
        cookies[i['name']] = i['value']
    return cookies
def getData(cookies):
    '''获取傲梦网站的学生信息以及课程信息
       返回获取数据的文件所在目录
       参数是网站所需的cookies
       数据的精细化处理  是数据的检索更加简单
    '''
    timec = time.strftime("%Y%m%d%H%M",time.localtime(time.time()))
    os.mkdir('./data/'+timec)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
    url = 'https://all-dream.com/rest/hour/queryMyCoursePlan4TeacherNew?free=0&limit=10&random=0.5043750329478451&page=1'
    today_class = requests.get(url,headers=headers,cookies=cookies)
    today_class = json.loads(today_class.text)
    print(today_class)
    with open('./data/'+timec+'/今日课程计划','wb') as file:
        pickle.dump(today_class,file)
    url_list = ['https://all-dream.com/rest/courseManage/queryMyOverCourse4Teacher?limit=10&page={}'.format(i+1)  for i in range(10)]
    over_all_class = []
    for url in url_list:
        over_class = requests.get(url,headers=headers,cookies=cookies)
        data_1 = json.loads(over_class.text)['list']
        over_all_class.append(data_1)
    key = 1
    stOverClass = {}
    for ondPage in over_all_class:
        for oneClass in ondPage:
            stOverClass[key]=oneClass
            key+=1
    df = pd.DataFrame(stOverClass).T

    with open('./data/'+timec+'/已完成课程','wb',) as file2:
        pickle.dump(df,file2)
    return timec

#生成了所有权限关闭的权限
class Friends():
    def __init__(self):
        with open('./data/好友信息','rb',) as file2:
            self.df =pickle.load(file2)
    def isvip(self,fromusername):
        '''对于主机微信的响应选择忽略
            在admin中有备案的用户是vip权限《傲梦教师》
            普通永用户都是nomal
        '''
        flag = False
        try:
            name = self.df[self.df['UserName'] == fromusername].index[0]
        except:
            flag = '主机微信'
            name = '两岸猿声啼不住'
        if name in [x[:-3] for x in message]:
            flag = True
        return flag

class Teacher():
    def __init__(self,username):
        self.username = username
        self.df = pd.read_pickle('./data/好友信息')
        self.name = self.df[self.df['UserName']==self.username].index[0]
        for i in message:
            if self.name in i:
                self.admin = message[i]
        print(self.name)
    def getcookies(self):
        '''
           验证码图片的微信发送
           验证码保存在本地   文件名由当前时间命名
           时间作为发送信息的图片名
        '''
        self.img_time = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
        if getimg(self.img_time):
            return self.img_time
    def svtime(self,timec):
        self.timec = timec

class Nomal():
    '''只要是主机微信的好友都是此类'''
    def __init__(self,username):
        self.flag = False
        self.username = username
def logdata(user):
    driver.close()
    itchat.send_msg(msg_to_u[3], user.username)
    timec = getData(user.cookies)
    itchat.send_msg(msg_to_u[4], user.username)
    return timec

class newTeacher():
    def __init__(self,user):
        self.id = user.username
        self.name = self.getname()
        self.num = self.getnum()
    def getname(self):
        df = pd.read_pickle('./data/好友信息')
        return  df[df['UserName']==self.id].index[0]
    def getnum(self):
        df = pd.read_pickle('./data/admin')
        if len(df)<10:
            result = '00'+str(len(df))
        elif len(df)<100:
            result = '0'+str(len(df))
        elif len(df) < 1000:
            result = str(len(df))
        return result

        return len(df)
    def savemsg(self):
        a = pd.read_pickle('./data/admin')
        a[self.name+str(self.num)] = [self.admin,self.password]
        with open('./data/admin','wb') as file:
            pickle.dump(a,file)
            print('信息录入成功')
@itchat.msg_register(itchat.content.TEXT)
def text(msg):
    global fsflag,timec,message
    message = readsth()
    # print(message)
    friend = Friends()
    '''控制台的函数控制
       信息的持续接收
    '''
    #print(friend.df)
    fromusername = msg['FromUserName']
    #此处可以增加管理员微信
    if msg['Text']=='初始化~':
        friends = itchat.get_friends(update=True)[1:]
        fsflag = initset(friends)
        return '初始化成功'
    elif '低价机票' in msg["Text"]:
        return getLowerAir(msg["Text"].replace('的低价机票',''))
    #图灵机器人模式
    elif msg['Text'] in ['开始','start']:
        fsflag[fromusername]['tuling'] = 'True'
        itchat.send_msg('ok~ next begin chat with Small~ Q from tu ling',fromusername)
    elif fromusername in fsflag:
        if fsflag[fromusername]['tuling']:
            if msg['Text'] in ['退出','exit']:
                fsflag[fromusername]['tuling'] = False
                return 'maybe! this the time leave u .Qqz'
            else:
                return jqr(msg['Text']) + "."
        elif fsflag[fromusername]['duniang']:
            if msg['Text'] == '退出百度':
                fsflag[fromusername]['duniang'] = False
                return 'see you my baby'
            else:
                return baidu(msg['Text']) + "."
        #度娘模式
        elif msg['Text'] in ['度娘','百度一下']:
            fsflag[fromusername]['duniang'] = 'True'
            itchat.send_msg('ok~ next begin chat with Small~ Q and baidu zhidao',fromusername)
        elif msg['Text'] == '热点':
            day,week = getnews()
            print(day,'\n',week)
            itchat.send_msg(day, fromusername)
            itchat.send_msg(week, fromusername)

        elif friend.isvip(fromusername):
            user = Teacher(fromusername)
            user.msg_1 = msg
            if user.msg_1['Text'] == '获取数据':
                itchat.send_msg('请耐心等候，小爬虫正在快吗加鞭获取数据', user.username)
                shot_tm = user.getcookies()
                itchat.send_msg(msg_to_u[1],user.username)
                itchat.send_image('.\image\{}1.png'.format(shot_tm),user.username)
            elif user.msg_1['Text'] in ['help', '帮助']:
                itchat.send_image('./image/teacher.png',user.username)
            elif re.findall('\d+',user.msg_1['Text']):
                if len(re.findall('\d+',user.msg_1['Text'])[0])==4:
                    user.yzm = re.findall('\d+',user.msg_1['Text'])[0]
                    suss,user.cookies = log_web(user.admin,user.yzm)
                    if suss:
                        timec = logdata(user)
                        bkb(user, timec)
                    else:
                        itchat.send_msg('so sad~ 验证码输入错误，请重新获取数据', user.username)
                        driver.close()
            elif user.msg_1['Text'] in '近日课程计划':
                print(timec)
                user.closetoday = getToday(timec,True)
                itchat.send_msg(user.name[:-4]+user.closetoday,user.username)

            elif user.msg_1['Text'] in '今日课程计划':
                print(timec)
                user.today = getToday(timec,False)
                itchat.send_msg(user.name[:-4]+user.today,user.username)
            elif user.msg_1['Text'][-4:]=='课堂反馈':
                ms = getfk(user.msg_1['Text'][:-4],timec)
                print(user.msg_1['Text'][:-4])
                if len(ms)>=1:
                    itchat.send_msg('已为您匹配到{}个结果'.format(len(ms)),user.username)
                    for ms_1 in ms:
                        itchat.send_msg(ms_1,user.username)
                else:
                    itchat.send_msg(msg_to_u[-1],user.username)
                for msg in ms:
                    itchat.send_msg(ms,user.username)

            elif '备课表' in user.msg_1['Text']:
                itchat.send_file('./data/' +user.username[-5:]+ '_alldream.xlsx',user.username)
        else:
            nomal = Nomal(msg['FromUserName'])
            print('创建聊天')
            nomal.msg = msg
            if nomal.msg['Text'] in ['help','帮助']:
                itchat.send_image('./image/nomal.png',nomal.username)
            if nomal.msg['Text'] == '注册傲梦讲师':
                global teacher
                teacher = newTeacher(nomal)
                itchat.send_msg('{}你好，现在需要录入你的傲梦网站的账号密码，请严格按照以下格式发送账号和密码（用一个空格隔开,前后不要加空格）如：”19091956102 12345“'.format(teacher.name),nomal.username)
            elif nomal.msg['Text'] == '初始化':
                initset()
            try:
                if nomal.username == teacher.id:
                    print(nomal.msg['Text'])
                    if len(nomal.msg['Text'].split(' '))==2 and len(nomal.msg['Text'].split(' ')[0])==11:
                        print(nomal.msg['Text'].split(' ')[0])
                        teacher.admin = nomal.msg['Text'].split(' ')[0]
                        teacher.password = nomal.msg['Text'].split(' ')[1]
                        itchat.send_msg('你确认账号密码无误？有误的话请重新注册无误请回复：信息无误请录入',nomal.username)
                    elif nomal.msg['Text'] == '信息无误请录入':
                        teacher.savemsg()
                        itchat.send_msg('录入成功',teacher.id)
            except:
                ...
