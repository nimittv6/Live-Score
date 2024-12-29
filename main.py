import requests
from bs4 import BeautifulSoup

url = "https://www.goal.com/en-in/live-scores"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

print(soup.prettify())