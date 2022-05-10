from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import pandas as pd

f = open('./Login_info.txt', 'r')
lines = f.readlines()
info=[]
for line in lines:
    line = line.strip()
    info.append(line)
f.close()

ID=info[1]
PW=info[3]

path = "./chromedriver.exe"
driver = webdriver.Chrome(path)
driver.implicitly_wait(1)

driver.get('https://success.gntech.ac.kr/login/a/n/login.do?requestKind=2')

driver.find_element(By.XPATH,'//*[@id="userId"]').send_keys(ID)
driver.find_element(By.XPATH,'//*[@id="userPw"]').send_keys(PW)
driver.find_element(By.XPATH,'//*[@id="loginBtn"]').click()

driver.find_element(By.XPATH,'//*[@id="pp_container"]/section/section[2]/a[2]/h3').click()
driver.maximize_window()
driver.find_element(By.XPATH,'//*[@id="MNU0000390"]/a').click()

pt1 = int(driver.find_element(By.XPATH,'//*[@id="certi1"]/dl/dd/p[2]/span').text)
pt2 = int(driver.find_element(By.XPATH,'//*[@id="certi2"]/dl/dd/p[2]/span').text)
pt3 = int(driver.find_element(By.XPATH,'//*[@id="certi3"]/dl/dd/p[2]/span').text)
pt4 = int(driver.find_element(By.XPATH,'//*[@id="certi4"]/dl/dd/p[2]/span').text)
pt5 = int(driver.find_element(By.XPATH,'//*[@id="certi5"]/dl/dd/p[2]/span').text)

pt_list=[[pt1], [pt2], [pt3], [pt4], [pt5], [None, None]]
pass_num = 0
for i in range(5):
    if pt_list[i][0]<5:
        pt_list[i].append(5-pt_list[i][0]) 
        pt_list[i].append("부족") 
    else:
        pt_list[i].append(0)
        pt_list[i].append("이수")
        pass_num+=1
        
pt_list[5].append("가능") if pass_num>=3 else pt_list[5].append("불가능")

pt_pd = pd.DataFrame(pt_list,index=['진로상담','글로벌','창의학습','봉사/인성', '취창업', '졸업여부'], columns=["보유 P", "부족 P", "현황"])
pt_pd.to_excel('./(구)과기대 SUCCESS 포인트 정리.xlsx')

driver.quit()
