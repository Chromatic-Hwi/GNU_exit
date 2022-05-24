from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

f = open('./Login_info.txt', 'r')
lines = f.readlines()
info=[]
for line in lines:
    line = line.strip()
    info.append(line)
f.close()

ID=info[1]
PW=info[5]

def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

driver=set_chrome_driver()
driver.implicitly_wait(5)

driver.get('https://accounts.gnu.ac.kr/common/login/login.do?service=https://nerum.gnu.ac.kr/sso/apiTest.jsp')
driver.maximize_window()

driver.find_element(By.XPATH,'//*[@id="userId"]').send_keys(ID)
driver.find_element(By.XPATH,'//*[@id="password"]').send_keys(PW)
driver.find_element(By.XPATH,'/html/body/div[3]/section/div/div[1]/div/div[1]/a/span').click()
time.sleep(0.5)
driver.find_element(By.XPATH,'//*[@id="gnb"]/ul/li[1]/a').click()
time.sleep(0.5)
driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/aside/nav/ul/li[2]/p/a').click()
driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/aside/nav/ul/li[2]/div/ul/li[2]/a').click()



N=1
while(True):
    try:
        Pro_Name=str(driver.find_element(By.XPATH,'//*[@id="tilesContent"]/div[2]/table/tbody/tr['+str(N)+']/td[1]/a').text)
        if Pro_Name=="2022년 폭력예방교육":
            break
        else:
            time.sleep(0.5)
            N+=1
    except NoSuchElementException:
            print("폭력예방교육을 신청하지 않으신 것 같습니다.")
            driver.quit()

driver.find_element(By.XPATH,'//*[@id="tilesContent"]/div[2]/table/tbody/tr['+str(N)+']/td[7]/a').click()
time.sleep(0.5)

Tab_Address = driver.window_handles
time.sleep(0.5)
driver.switch_to.window(Tab_Address[1])
time.sleep(0.5)
driver.find_element(By.XPATH,'//*[@id="sidenav"]/nav/ul/div/ul/li[2]/a').click()

for i in range(2, 27):
    CHECK = str(driver.find_element(By.XPATH,'//*[@id="learning_list"]/tbody/tr['+str(i)+']/td[6]/span').text)
    if CHECK=="출석완료":
        pass
    else:
        T=driver.find_element(By.XPATH,'//*[@id="learning_list"]/tbody/tr['+str(i)+']/td[4]').text
        T=int(T[:-1]) 
        T_Final=T*60+60 
        driver.find_element(By.XPATH,'//*[@id="learning_list"]/tbody/tr['+str(i)+']/td[7]/a[1]').click()
        time.sleep(T_Final) 
        driver.find_element(By.XPATH,'//*[@id="btn_list"]').click()
    
driver.quit()

