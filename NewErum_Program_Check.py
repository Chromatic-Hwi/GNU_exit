from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

f = open('./Login_info.txt', 'r')
lines = f.readlines()
info=[]
for line in lines:
    line = line.strip()
    info.append(line)
f.close()

ID=info[1]
PW=info[5]

path = "./chromedriver.exe"
driver = webdriver.Chrome(path)
driver.implicitly_wait(1)

driver.get('https://accounts.gnu.ac.kr/common/login/login.do?service=https://nerum.gnu.ac.kr/sso/apiTest.jsp')
driver.maximize_window()

driver.find_element(By.XPATH,'//*[@id="userId"]').send_keys(ID)
driver.find_element(By.XPATH,'//*[@id="password"]').send_keys(PW)
driver.find_element(By.XPATH,'//*[@id="content"]/div[1]/div/a').click()

driver.find_element(By.XPATH,'//*[@id="gnb"]/ul/li[1]/a').click()

driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/aside/nav/ul/li[2]/p/a').click()
driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/aside/nav/ul/li[2]/div/ul/li[1]/a').click()
