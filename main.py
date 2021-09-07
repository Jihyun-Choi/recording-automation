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
driver.implicitly_wait(time_to_wait=5)
driver.find_element_by_xpath('//*[@id="modalPush"]/div/div/div[1]/button/span[2]').click()
driver.find_element_by_xpath('/html/body/div[2]/div/div/section/div/div/div/div[1]/div/div[2]/h3/strong/a').click()

driver.implicitly_wait(time_to_wait=5)

# driver.find_element_by_xpath('**').send_keys('ID/PW')로 입력 ----개인정보 보호!!
driver.find_element_by_xpath('//*[@id="one_id"]').send_keys('ID 작성')
driver.find_element_by_xpath('//*[@id="password"]').send_keys('PW 작성')

# 오류난 코드들
# id = driver.find_element_by_xpath('//*[@id="one_id"]')
# id.click()
# id.send_keys('ID') #아이디 적기
# pw = driver.find_element_by_xpath('//*[@id="password"]')
# pw.click()
# pw.send_keys('PW') # 비밀번호 적기

action.key_down(Keys.ENTER).perform()
action.key_up(Keys.ENTER).perform()

driver.implicitly_wait(time_to_wait=10)
driver.find_element_by_xpath('//*[@id="course-link-_233939_1"]').click()

driver.implicitly_wait(time_to_wait=10)

# 마우스 좌표값을 출력해 pg로 클릭하기
# print(pg.position())
time.sleep(3)
pg.moveTo(pg.position(182, 445))
pg.click(pg.position(182, 445))

i = 1
iframes = driver.find_element_by_tag_name('iframe')
driver.switch_to.frame(iframes)


# driver.find_element_by_xpath('//*[@id="paletteItem:_3917138_1"]/a/span').click()
driver.find_element_by_link_text('온라인강의_'+str(i)).click()
driver.implicitly_wait(time_to_wait=10)
# driver.find_element_by_link_text('XIN - 컴넷_온라인_1 / 2021-09-02 00:00 ~ 2021-09-03 23:59').click()

iframes = driver.find_element_by_tag_name('iframe')
driver.switch_to.frame(iframes)
driver.find_element_by_xpath('//*[@id="anonymous_element_7"]/a/span').click()



# 오류
# iframes = driver.find_element_by_tag_name('iframe')
# driver.switch_to.frame(iframes)
# driver.find_element_by_xpath('//*[@id="paletteItem:_3917138_1"]/a/span').click()
#
#
# driver.find_element_by_xpath('//*[@id="anonymous_element_7"]/a/span').click()
# #
# # //*[@id="anonymous_element_7"]/a/span
# # //*[@id="anonymous_element_9"]/a/span



# 제대로 되었는지 확인 후 3초 뒤 창 끄기
# time.sleep(3)
# driver.close()