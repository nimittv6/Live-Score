import requests
from bs4 import BeautifulSoup
from lxml import etree
url = "https://www.goal.com/en-in/live-scores"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

dom = etree.HTML(str(soup))

live_Score = (dom.xpath('//*[class="live-scores_live-scores-wrapper__lGxsb"]/text'))
print(live_Score)