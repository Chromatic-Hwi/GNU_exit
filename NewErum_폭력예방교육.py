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




# 이러닝 강의실로 이동
driver.find_element(By.XPATH,'//*[@id="tilesContent"]/div[2]/table/tbody/tr[3]/td[7]/a').click()

# 현재 열린 탭들의 주소를 리스트로 반환, 그중 두번째 즉 새로 열린 탭을 선택하기 위함.
Tab_Address = driver.window_handles

# 탭 전환
driver.switch_to.window(Tab_Address[1])

driver.find_element(By.XPATH,'//*[@id="sidenav"]/nav/ul/div/ul/li[2]/a').click()

# 총 강의수는 25개
for i in range(2, 27):
    CHECK = str(driver.find_element(By.XPATH,'//*[@id="learning_list"]/tbody/tr['+str(i)+']/td[6]/span').text)
    if CHECK=="출석완료":
        pass
    else:
        T=driver.find_element(By.XPATH,'//*[@id="learning_list"]/tbody/tr['+str(i)+']/td[4]').text
        T=int(T[:-1]) # 강의 길이에 해당하는 분이 나옴.
        T_Final=T*60+10 # 강의 시간 +10초를 통해 동작 여유시간을 줌
        driver.find_element(By.XPATH,'//*[@id="learning_list"]/tbody/tr['+str(i)+']/td[7]/a[1]').click()
        time.sleep(T_Final) # 강의가 재생될테니 sleep을 걸어줌
        driver.find_element(By.XPATH,'//*[@id="btn_list"]').click() # 시간이 지나면 [목록] 클릭
    
driver.quit() # 학습 완료후 종료
