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
from turling import jqr
import itchat
from Find import *
message = readsth()
msg_to_u = ['你好呀！现在开启微信机器人啦\n你可以获取数据','正在进入网页\n你可能需要根据图片输入验证码','正在获取cookies请稍等',' 已成功获取到cookies，\n接下来我要把所有的数据进行抓取','数据已经被我们完美的爬取下来\n接下来我们可以对数据进行一个查看或者操作\n今日课程计划\n某某同学的课堂反馈\n备课表的在线生成','\n  今日热点','  今日热点\n','     早安\n','    晚安','很抱歉，未找到任何关于这个学生的历史课堂，请检查学生姓名是否输入错误']
driver = ''
pic_xpth = '//*[@id="teacher_form"]/div[2]/div/img'
us_xpath = '//*[@id="teacher_form"]/div[2]/input[1]'
ps_xpath = '//*[@id="teacher_form"]/div[2]/input[3]'
yzm_xpath = '//*[@id="teacher_form"]/div[2]/input[4]'
dl_xpath = '//*[@id="teacher_form"]/input[2]'
def getnews():
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
class Friends():
    def __init__(self):
        with open('./data/好友信息','rb',) as file2:
            self.df =pickle.load(file2)
    def isvip(self,fromusername):
        username = self.df[self.df['Remark'].isin(list(message.keys()))]['UserName'].values
        if fromusername in username:
            return True
        else:
            return False

    def readvip():
        pass
class Teacher():
    def __init__(self,username):
        self.username = username
        with open('./data/好友信息','rb',) as file2:
            self.df =pickle.load(file2)
        self.name = self.df[self.df['UserName']==self.username].iloc[0].Remark
        self.admin = message[self.name]
        print(self.name)
    def getmessage(self,flag):
        if self.msg_1['Text'] =='小小奇':
            flag = True
        return flag
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
    def __init__(self,username):
        self.flag = False
        self.username = username
def logdata(user):
    driver.close()
    itchat.send_msg(msg_to_u[3], user.username)
    timec = getData(user.cookies)
    itchat.send_msg(msg_to_u[4], user.username)
    return timec
nomalflag = {}
userflag = {}
@itchat.msg_register(itchat.content.TEXT)
def text(msg):
    global userflag,timec,nomalflag
    friend = Friends()
    '''控制台的函数控制
       信息的持续接收
    '''
    #print(friend.df)
    fromusername = msg['FromUserName']
    if friend.isvip(fromusername):
        user = Teacher(fromusername)
        user.msg_1 = msg
        if user.msg_1['Text'] in ['start','小小奇','开始']:
            itchat.send_msg('以下内容是自动回复,发送“exit”或者“退出”退出退出自动回复',user.username)
            userflag[user.username] = True
        elif user.msg_1['Text'] in ['end','exit','退出']:
            userflag[user.username] = False
        if len(userflag):
            if userflag[user.username]:
                itchat.send_msg(jqr(user.msg_1['Text'])+".",user.username)

        if len(userflag)==0 or userflag[user.username]==False:
            if user.msg_1['Text'] == '获取数据':
                itchat.send_msg('请耐心等候，小爬虫正在快吗加鞭获取数据', user.username)
                shot_tm = user.getcookies()
                itchat.send_msg(msg_to_u[1],user.username)
                imgnum = aiYzm('.\image\{}1.png'.format(shot_tm))
                if imgnum:
                    user.yzm = imgnum
                    suss, user.cookies = log_web(user.admin, user.yzm)
                    if suss:
                        itchat.send_msg('网站登录成功，请稍等片刻数据马上抓取成功', user.username)
                        timec = logdata(user)
                        bkb(user, timec)

                    else:
                        itchat.send_msg('so sad~ 验证码自动识别失败，请重新获取数据', user.username)
                        driver.close()

                else:
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
            elif user.msg_1['Text'] == '热点':
                day,week = getnews()
                print(day,'\n',week)
                itchat.send_msg(day, user.username)
                itchat.send_msg(week, user.username)
            elif '备课表' in user.msg_1['Text']:
                itchat.send_file('./data/' + user.name[-4:] + 'alldream.xlsx',user.username)
    else:
        nomal = Nomal(msg['FromUserName'])
        print('创建聊天')
        nomal.msg = msg
        if nomal.msg['Text'] in ['start','小小奇','开始']:
            itchat.send_msg('以下内容是自动回复,发送“exit”或者“退出”退出退出自动回复',nomal.username)
            nomalflag[nomal.username] = True
        elif nomal.msg['Text'] in ['help','帮助']:
            itchat.send_image('./image/nomal.png',nomal.username)
        elif nomal.msg['Text'] in ['end','exit','退出']:
            nomalflag[nomal.username] = False
        try:
            if nomalflag[nomal.username]:
                itchat.send_msg(jqr(nomal.msg['Text'])+".",nomal.username)
        except:
            pass
        print(nomal.username,nomal.msg)
        print(nomalflag)