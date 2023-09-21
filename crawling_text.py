from selenium import webdriver
from selenium.webdriver.common.keys import Keys # 키보드 역할
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import openpyxl
import pandas as pd
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



options = Options()
# options.add_argument('--headless') # 백그라운드 실행
options.add_experimental_option("detach", True)
options.add_argument("--disable-popup-blocking") # 팝업 차단

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# 페이지 로딩이 완료될 때까지 기다리는 코드
# driver.implicitly_wait(3)

# 사이트 접속하기
driver.get('https://www.riss.kr/')

# 메인 창 핸들 저장
main_window_handle = driver.window_handles[0]

# 팝업 창으로 스위치
driver.switch_to.window(driver.window_handles[1])

# 팝업 창 닫기
driver.close()

# 다시 메인 창으로 스위치
driver.switch_to.window(main_window_handle)


"""
<input type="text" id="query" name="query" placeholder="무엇을 찾고 계세요?" title="검색" onkeydown="javascript:setFrameEvent(event);" onkeyup="javascript:getAutoQuery(this.value,event);" onblur="javascript:onBlurCheck();document.getElementById('lastFocusName').value='query';" onkeypress="javascript:trick();" tabindex="22">
"""
# driver.find_element(By.CLASS, "").send_keys("GPT")
search = driver.find_element(By.XPATH, '//*[@id="query"]')
search.send_keys("GPT")
search.send_keys(Keys.RETURN) # 또는 search.send_keys('\n')

time.sleep(1)

# 국내학술논문 탭 클릭
driver.find_element(By.XPATH, '//*[@id="tabMenu"]/ul/li/div/ul/li[2]/a/span').click()



# 출력 갯수를 100개로 변경
driver.find_element(By.XPATH, '//*[@id="divContent"]/div/div[2]/div/div[3]/div[1]/div[2]/div[3]/div[1]').click()
driver.find_element(By.XPATH, '//*[@id="divContent"]/div/div[2]/div/div[3]/div[1]/div[2]/div[3]/div[2]/div/ul/li[5]/a').click()
driver.find_element(By.XPATH, '//*[@id="divContent"]/div/div[2]/div/div[3]/div[1]/div[2]/button').click()


"""
while True:
    bh = driver.execute_script("return document.body.scrollHeight") # 브라우저 상의 처음 높이
    print(bh)
    time.sleep(4)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # 스크롤 내리기
    time.sleep(2)
    ah = driver.execute_script("return document.body.scrollHeight")
    if ah == bh:
        break

papers = []

paper_elements = driver.find_element(By.CSS_SELECTOR, '.srchResultListW')
for paper_element in paper_elements:
    paper_info = {}
    paper_info["논문 제목"] = paper_element.find_element(By.CSS_SELECTOR, '.srchResultListW > ul > li > .cont > .title').text
    paper_info["저자"] = paper_element.find_element(By.CSS_SELECTOR, '.srchResultListW > ul > li > .cont > .etc > span:first-child').text
    paper_info["출판사"] = paper_element.find_element(By.CLASS_NAME, "assigned").text
    # paper_info["연도"] = paper_element.find_element(".etc > p:nth-child(3)").text
    papers.append(paper_info)
"""

# 스크롤을 내리면서 논문 정보 크롤링
papers = []

while True:
    bh = driver.execute_script("return document.body.scrollHeight") # 브라우저 상의 처음 높이
    print(bh)
    time.sleep(4)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # 스크롤 내리기
    time.sleep(2)
    ah = driver.execute_script("return document.body.scrollHeight")
    if ah == bh:
        break

paper_elements = driver.find_elements(By.CSS_SELECTOR, ".srchResultListW > ul > li")


for paper_element in paper_elements:
    
    try:
        paper_info = {}
        paper_info["논문 제목"] = paper_element.find_element(By.CSS_SELECTOR, '.title').text
        paper_info["저자"] = paper_element.find_element(By.CSS_SELECTOR, '.writer').text
        paper_info["출판사"] = paper_element.find_element(By.CSS_SELECTOR, '.assigned').text
        paper_info["연도"] = paper_element.find_element(By.CSS_SELECTOR, '.etc').text
        papers.append(paper_info)
    
    except:
        print('Exception')


# 데이터를 데이터프레임으로 저장
df = pd.DataFrame(papers)

# 엑셀 파일로 저장
df.to_excel("GPT_papers.xlsx", index=False)

# 브라우저 종료
driver.quit()


# 화면 꺼짐 방지
# while True:
#     pass