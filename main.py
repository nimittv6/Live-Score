import requests
from bs4 import BeautifulSoup
from lxml import etree
url = "https://www.goal.com/en-in/live-scores"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

dom = etree.HTML(str(soup))

live_Score = (dom.xpath('//*[@id="__next"]/div[1]/div[2]/div[2]/main/section/section'))
print(live_Score)