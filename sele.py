from selenium import webdriver
from selenium.webdriver.common.keys import Keys # 키보드 역할
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


options = Options()
# options.add_argument('--headless') # 백그라운드 실행
options.add_experimental_option("detach", True)

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# 페이지 로딩이 완료될 때까지 기다리는 코드
# driver.implicitly_wait(3)

# 사이트 접속하기
driver.get('https://www.google.com')

"""
<textarea jsname="yZiJbe" class="gLFyf" jsaction="paste:puy29d;" id="APjFqb" maxlength="2048" name="q" rows="1" aria-activedescendant="" aria-autocomplete="both" aria-controls="Alh6id" aria-expanded="false" aria-haspopup="both" aria-owns="Alh6id" autocapitalize="off" autocomplete="off" autocorrect="off" autofocus="" role="combobox" spellcheck="false" title="검색" type="search" value="" aria-label="검색" data-ved="0ahUKEwjQ9paFzJaBAxVqh1YBHQ9pBdYQ39UDCAY" style=""></textarea>

"""
#driver.find_element(By.CLASS_NAME, "gLFyf").send_keys("BTS")
search = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
search.send_keys("BTS")
search.send_keys(Keys.RETURN) # 또는 search.send_keys('\n')

time.sleep(1)



# 화면 꺼짐 방지
while True:
    pass