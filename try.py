import requests
import json
from bs4 import BeautifulSoup
from lxml import etree
from pyspider.libs.base_handler import *


# from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
#
# bro=webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
# wait1=WebDriverWait(bro,20)
# bro.get('https://www.jin10.com/')
# wait=WebDriverWait(bro,10)
# print(bro.page_source)
# header={
#     'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
# }
# r=requests.get('http://www.jin10.com',headers=header)
# print(r.json())
# soup=BeautifulSoup(r.content,"html5lib")
# print(soup.prettify())
# html=etree.HTML(r.content,parser=etree.HTMLParser(encoding='utf-8'))
# print(html)
# id_list=html.xpath('//div[@class="jin-flash_wrap J_flash_wrap is-show"]/div[@id]/@id')
# for i in id_list:
#     print(i)
