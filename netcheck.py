# coding:utf-8
import os
import time
from datetime import datetime
startnet='netsh interface set interface name="乙太網路" admin=enable'
stopnet='netsh interface set interface name="乙太網路" admin=disable'
trynet1='ping google.com'
trynet2='ping 210.240.163.26'
path = 'C:/Users/BEAR/Desktop/netlog.txt'
while True:
    try:
        result1=os.system(trynet1)
        result2=os.system(trynet2)
        now=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if(result1==0 and result2==0):#網路正常
            print(f'{now} 網路一切正常')
            with open(path, 'a') as f:
                f.write(f'{now} 網路一切正常\n')
        else:#網路異常 停用&啟用網卡
            result2=os.system(stopnet)
            print(f'{now} 網路異常，正在關閉網卡')            
            with open(path, 'a') as f:
                f.write(f'{now} 網路異常，正在關閉網卡\n')
            time.sleep(20)
            result2=os.system(startnet)
            print(f'{now} 網路異常，重新啟動網卡')
            with open(path, 'a') as f:
                f.write(f'{now} 網路異常，重新啟動網卡\n')
        time.sleep(300)
    except:
        break