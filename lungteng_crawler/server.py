#code by fan_31
import requests
from bs4 import BeautifulSoup
import os
import time

#Line Notify封包
headers = {
        "Authorization": "Bearer " + "SQsf4gSmwpI9Z16I08p7hVCKWy1XzLDxB1RXgF27WrG",
        "Content-Type": "application/x-www-form-urlencoded"
    }
#Line Notify發送通知
params = {"message": "\n server start success!!"}
#/////////////////////////////////////////////////////////////////////////////////////////////////
r = requests.post("https://notify-api.line.me/api/notify",
                      headers=headers, params=params)
print(r.status_code)  #200
login_URL = 'https://eo.lungteng.com.tw/Home/Login'
target = 'https://eo.lungteng.com.tw/Student/Exam'
#login
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    }
formdata = {
    'account':' 輸入帳號 ',
    'password':' 輸入密碼 ',
    }

rename = "non"
name = "non"
while True:
    session = requests.Session()
    session.post(login_URL, headers = headers, data = formdata)#login
#get web html
    r = session.get(target, headers = headers)
    print("requests sent!!")
#save web html as web_html.txt
    f = open("web_html.txt", "a", encoding = "utf-8")#建立網頁資料的文字檔(web_html.txt)
    f.write("".join(r.text))#匯出網頁資料
    f.close()
#//////////////////////////////////////////////////////////////////////////////////////
    rename = name
#get information
    soup = BeautifulSoup(r.text,"html.parser") #將網頁資料以html.parser
#///////////////////////////資料
    exc = soup.select("table.table td") #取HTML標中的
    #print the information
    num = 1
    er=[0]*100
    for i in exc:
        #print(i.text)
        er[num] = str(i.text)
        num+=1

    ter = int(er[4])
    #print(ter)
#//////////////////////////////////////////////////////////////////////////////////////////
    if ter>= 1:
        #/////////////////////截止時間(exam.lstrip())
        #get exam information
        exam = soup.select("table.table p") #取HTML標中的
        #print the information
        t = 1
        et=[0]*100
        for e in exam:
            et[t] = str(e.text).lstrip()
            exam = et[t]
            t+=1
            #print("et["+str(t)+"] = "+exam)
            exam1 = et[2]
            exam2 = et[4]
            exam = et[2]

#/////////////////////考試名稱(e[6].strip()) (name)
        exc = soup.select("table.table td") #取HTML標中的
#print the information
        num = 1
        ex=[0]*100
        for i in exc:
            #print(i.text)
            ex[num] = str(i.text)
            num+=1
        if len(ex[6].strip()) != 0:
            name = ex[6].strip()
            total = 1
        else:
            name1 = ex[9].strip()
            name2 = ex[15].strip()
            name = ex[9].strip()
            total = 2
        print("total = " + str(total))
#        print(ex[6].strip())
#//////////////////////get 時間h, m, s(時, 分, 秒)
        localtime = time.localtime()
        h = int(time.strftime("%H", localtime))
        m = int(time.strftime("%M", localtime))
        s = int(time.strftime("%S", localtime))
#        print(h, m ,s)

        if h==18 and m==0:
            rename = "non"


        if name != rename:
#Line Notify封包&發送通知
            headers = {
                    "Authorization": "Bearer " + " 輸入 line notify 權杖 ",
                    "Content-Type": "application/x-www-form-urlencoded"
                }
            if total == 1:
                params = {"message": "考試: " + name + "\n截止時間: " + exam.lstrip()}
                r = requests.post("https://notify-api.line.me/api/notify", headers=headers, params=params)
                print(r.status_code)  #200
            elif total == 2:
                params = {"message": "考試: " + name1 + "\n截止時間: " + exam1.lstrip()}
                r = requests.post("https://notify-api.line.me/api/notify", headers=headers, params=params)
                print(r.status_code)  #200
                params = {"message": "考試: " + name2 + "\n截止時間: " + exam2.lstrip()}
                r = requests.post("https://notify-api.line.me/api/notify", headers=headers, params=params)
                print(r.status_code)  #200
            else:
                print("unknow error!!")
        else:
            print(name + "," + rename)
        time.sleep(50)
    else:
        print("shit there is no test!")
        time.sleep(120)
    os.remove(r"web_html.txt")
