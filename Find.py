import pandas as pd
import pickle
import time


def aiYzm(filename):
    '''
    :param filename: 表示图片的文件路径
    :return: 返回图片经过百度开发识别的结果，如识别失败的话直接返回false
    '''
    from aip import AipOcr
    """ 你的 APPID AK SK """
    APP_ID = '16190824'
    API_KEY = 'sW2uzXjyWqiyC5Lq2lNsdnig'
    SECRET_KEY = 'GVF2YX5cS7RZqfXMGgIpnuPDPQyfEyWq'
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    """ 读取图片 """
    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()
    image = get_file_content(filename)
    """ 调用数字识别 """
    client.numbers(image);
    """ 如果有可选参数 """
    options = {}
    options["recognize_granularity"] = "big"
    options["detect_direction"] = "true"
    """ 带参数调用数字识别 """
    a = client.numbers(image, options)
    try:
        a = a['words_result'][0]['words']
        print(a)
    except:
        return False
    else:
        if len(a) == 4:
            return a
        else:
            return False
def uTime(stamp):
    '''
    unix时间戳转化为正常显示的时间
    参数是时间戳
    返回值是转换好的时间
    '''
    stamp = stamp/1000
    time_local = time.localtime(stamp)
    df  = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
    return df
def bkb(user,timec):
    '''生成备课表'''
    filename = user.name
    with open('data/'+timec+'/'+'已完成课程', 'rb') as file:
        data = pickle.load(file)
    data = data[['courseTypeName', 'studentName', 'lessonStartTime', 'lessonEndTime', 'homework', 'recordUrl',
                 'teacherComment']]
    data = data[data['lessonStartTime'] >= int(time.time() - 604800) * 1000]
    data.columns = ['科目', '学生姓名', '课堂开始时间', '课堂结束时间', '课堂作业', '上课视频', '上课情况']
    class_time = []
    for i in data.index:
        time_1 = data.loc[i].课堂结束时间 - data.loc[i].课堂开始时间
        data.loc[i].课堂开始时间 = uTime(data.loc[i].课堂开始时间)
        data.loc[i].课堂结束时间 = uTime(data.loc[i].课堂结束时间)
        if time_1 >= 3600000:
            time_1 = 2
        else:
            time_1 = 1
        class_time.append(time_1)
        print(time_1)
    data.insert(4, '课时消耗', class_time)
    data.to_excel('./data/' + filename[-4:] + 'alldream.xlsx', 'w+')

def getToday(path,flag):
    '''参数是当前目录（今日学生信息的名称）下的文件名称
       返回值是一个字符串  包含今日未完成课程信息
       功能：获取当前日期内的上课内容
    '''
    if flag:
        tm = '近日'
    else:
        tm = '今日'
    str1 = ''
    with open('./data/'+path+'/今日课程计划','rb') as file:
        data = pickle.load(file)
    stlist = data['list']
    nowday = time.strftime("%Y-%m-%d",time.localtime(time.time()))
    times=0
    if not flag:
        for st in stlist:
            sttime = uTime(st['startTime'])
            if sttime[:10]!=nowday:
                continue
            times+=1
            edtime = uTime(st['endTime'])
            stname = st['studentName']
            kemu = st['courseTypeName']
            banji = st['courseHourName']
            str1 += '\t学生：{}   \n\t时间：\n\t{}\n\t{}   \n\t科目：\t{}   \n\t班级：{}\n'.format(stname,sttime,edtime,kemu,banji)
    else:
        for st in stlist:
            sttime = uTime(st['startTime'])
            times+=1
            edtime = uTime(st['endTime'])
            stname = st['studentName']
            kemu = st['courseTypeName']
            banji = st['courseHourName']
            str1 += '学生：{}   \n时间：\n{}\n{}   \n科目：{}   \n班级：{}\n'.format(stname,sttime,edtime,kemu,banji)

    if times >=1:
        return '老师您好，\n{}你总共有{}节课\n内容如下\n'.format(tm,times)+str1
    else:
        return'老师~今天真幸福呀,\n{}你已经完成了所有工作\n当然今天也可能是非常愉快的休息日，\n试试召唤智能机器人,\n  \"小小奇\" '.format(tm)
                
def getfk(name,timec):
    '''
    参数：查看反馈的学生姓名  以及保存本次数据的文件最内层路径
    返回值：包含匹配到该学生的三条数据  如果先搞改变匹配数据的数量只需要改掉times里的值
    功能实现原始数据的检索  可通过学生姓名直接检索
    '''
    with open('./data/'+timec+'/已完成课程','rb') as file:
        df = pickle.load(file)
    student = df[df['studentName']==name]
    msg_list = []
    for i in range(len(student)):
        st = student.iloc[i]
        remark = st['teacherComment']
        videourl = st['recordUrl']
        star = st['teacherCommentOne']
        stTime = st['lessonStartTime']
        msg = '这节课的开始时间是:\n{}\n这节课里你对孩子评价是：\n{}\n您为孩子打出惊人的{}颗星\n视频链接:\n{}\n--------------------------------------------'
        msg_one = msg.format(uTime(stTime),remark,star,videourl) 
        msg_list.append(msg_one)
    return msg_list
    
