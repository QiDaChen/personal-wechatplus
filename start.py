#author：magic Chen  py3.7.0  2019/3/25  chenphoun@outlook.com
import  itchat
from run import *
import pandas as pd 


def main():  
    itchat.auto_login(hotReload=True,enableCmdQR=2) 
    friends = itchat.get_friends(update=True)[1:]    
    dealData(friends)
    initset(friends)
    itchat.run()    
if __name__ == "__main__":
    main()
    
    
