import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import pyautogui as pg

URL = 'https://kulms.korea.ac.kr/ultra/course'
driver = webdriver.Chrome(executable_path=r'.\chromedriver.exe')
action = ActionChains(driver)
driver.maximize_window()
driver.get(url=URL)
driver.implicitly_wait(time_to_wait=15)
driver.find_element_by_xpath('//*[@id="modalPush"]/div/div/div[1]/button/span[2]').click()
driver.find_element_by_xpath('/html/body/div[2]/div/div/section/div/div/div/div[1]/div/div[2]/h3/strong/a').click()

driver.implicitly_wait(time_to_wait=5)

# driver.find_element_by_xpath('**').send_keys('ID/PW')로 입력 ----개인정보 보호!!

action.key_down(Keys.ENTER).perform()
action.key_up(Keys.ENTER).perform()

driver.implicitly_wait(time_to_wait=10)
driver.find_element_by_xpath('//*[@id="course-link-_233939_1"]').click()

driver.implicitly_wait(time_to_wait=10)

# 마우스 좌표값을 출력해 pg로 클릭하기
# print(pg.position())
# time.sleep(3)
# pg.moveTo(pg.position(182, 445))
# pg.click(pg.position(182, 445))

iframes = driver.find_element_by_tag_name('iframe')
driver.switch_to.frame(iframes)
driver.find_element_by_xpath('//*[@id="paletteItem:_3917138_1"]/a/span').click()
driver.switch_to.default_content() #원래 있던 전체 웹 페이지로 나오기

i = 3
driver.implicitly_wait(time_to_wait=10)
driver.switch_to.frame(iframes)

action.key_down(Keys.SPACE).perform()
action.key_up(Keys.SPACE).perform()

driver.find_element_by_link_text('온라인강의_'+i.__str__()).click()
driver.switch_to.default_content() #원래 있던 전체 웹 페이지로 나오기

driver.implicitly_wait(time_to_wait=10)
driver.switch_to.frame(iframes)
driver.find_element_by_xpath('//*[@id="anonymous_element_7"]/a/span').click()
driver.switch_to.default_content() #원래 있던 전체 웹 페이지로 나오기

# iframe 접근이 다른 것 같은데 오류가 난다.
# driver.implicitly_wait(time_to_wait=10)
# video_iframe = driver.find_elements_by_tag_name('share_iframe')
# driver.switch_to.frame(video_iframe)
# driver.find_element_by_xpath('//*[@id="front-screen"]/div/div[2]/div[1]/div').click()
# driver.switch_to.default_content() #원래 있던 전체 웹 페이지로 나오기


# 강의 녹화 시작하기
pg.hotkey('alt', 'tab')
time.sleep(1)
pg.click(pg.center(pg.locateOnScreen('record_start.png')))
pg.hotkey('alt', 'tab')


# 일시적으로 좌표값으로 클릭 추후에 xpath값으로 접근하도록 수정
# 강의 재생
driver.implicitly_wait(time_to_wait=10)
time.sleep(5)
pg.moveTo(pg.position(959, 581))
pg.click(pg.position(959, 581))

time.sleep(10)

# 강의가 끝날때까지 기다리기
while pg.locateOnScreen('video_end.png') == None:
        time.sleep(60)

# 강의 녹화 그만하기
pg.hotkey('alt', 'tab')
time.sleep(1)
pg.click(pg.center(pg.locateOnScreen('record_stop.png')))
pg.hotkey('alt', 'tab')

# 프로그램 종료
driver.close()