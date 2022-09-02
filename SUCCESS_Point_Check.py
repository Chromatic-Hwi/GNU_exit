from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
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

def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

driver=set_chrome_driver()
driver.implicitly_wait(5)

driver.get('https://success.gntech.ac.kr/login/a/n/login.do?requestKind=2')

driver.find_element(By.XPATH,'//*[@id="userId"]').send_keys(ID)
driver.find_element(By.XPATH,'//*[@id="userPw"]').send_keys(PW)
driver.find_element(By.XPATH,'//*[@id="loginBtn"]').click()

driver.find_element(By.XPATH,'//*[@id="pp_container"]/section/section[2]/a[2]/h3').click()
driver.maximize_window()
driver.find_element(By.XPATH,'//*[@id="MNU0000390"]/a').click()

try:
    pt1 = int(driver.find_element(By.XPATH,'//*[@id="certi1"]/dl/dd/p[2]/span').text)
    pt2 = int(driver.find_element(By.XPATH,'//*[@id="certi2"]/dl/dd/p[2]/span').text)
    pt3 = int(driver.find_element(By.XPATH,'//*[@id="certi3"]/dl/dd/p[2]/span').text)
    pt4 = int(driver.find_element(By.XPATH,'//*[@id="certi4"]/dl/dd/p[2]/span').text)
    pt5 = int(driver.find_element(By.XPATH,'//*[@id="certi5"]/dl/dd/p[2]/span').text)
    total_pt = pt1+pt2+pt3+pt4+pt5

    pt_list=[[pt1], [pt2], [pt3], [pt4], [pt5], [total_pt], [None, None]]
    pass_num = 0
    for i in range(5):
        if pt_list[i][0]<5:
            pt_list[i].append(5-pt_list[i][0]) 
            pt_list[i].append("미이수") 
        else:
            pt_list[i].append(0)
            pt_list[i].append("이수")
            pass_num+=1

    pt_list[5].append(0) if total_pt>=30 else pt_list[5].append(30-total_pt)
    pt_list[5].append("충족") if total_pt>=30 else pt_list[5].append("부족")
    pt_list[6].append("가능") if pass_num>=3 and total_pt>=30 else pt_list[6].append("불가능")

    pt_pd = pd.DataFrame(pt_list,index=["진로상담", "글로벌", "창의학습", "봉사/인성", "취창업", "P 총합", "졸업여부"], columns=["보유 P", "부족 P", "현황"])
    pt_pd.to_excel('./(구)과기대 SUCCESS 포인트 정리.xlsx')

except:
    f=open("./Error_History.txt", "a")
    f.write("Point save Error!!\n")
    f.write("Check account please.")
    f.close
    
driver.quit()
