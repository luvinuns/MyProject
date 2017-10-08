"""
import os
from selenium import webdriver
driver = webdriver.Chrome(os.path.abspath('chromedriver'))
driver.get('http://www.nwkyungsan.co.kr/s2/hp/stBoardL.asp…')
driver.switch_to.frame('mainFrame')
html = driver.page_source
print(html)
driver.close()
"""
import requests
import csv
from bs4 import BeautifulSoup #pip install beatifulsoup4

url = "http://goodmonitoring.com/monitor_board/"
html = requests.get(url).text
#print(html)

#iframe src 주소
board_url = "http://goodmonitoring.com/xe/moi"
html= requests.get(board_url).text
#print(html)



soup = BeautifulSoup(html, 'html.parser')
rows=[]
for tr_tag in soup.select('.bd_lst_wrp > table tbody tr'):
    cols=[]
    for td_tag in tr_tag.select('td'):
        cols.append(td_tag.text.strip())
    print(cols)
    rows.append(cols)


#with open("goodmonitoring.csv", "wt", encoding="utf-8", newline='') as f:     # 엑셀에서 한글깨짐
with open("goodmonitoring.csv", "wt", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)

#%ls
