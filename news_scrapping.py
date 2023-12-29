from time import sleep
from bs4 import BeautifulSoup
import requests
import textwrap

url = ("https://economictimes.indiatimes.com/news/india/bharats-coming-of-age-in-a-world-of-conflict-12-headlines-that-"
       "defined-2023/articleshow/106226561.cms")
website = requests.get(url)
soup = BeautifulSoup(website.content, "html.parser")
print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------    TOP NEWS OF 2023 FROM ECONOMIC TIMES    ----------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("\n")
for link in soup.findAll("ol"):
    storys = link.findAll("li")
    for news in storys:
        wrap = textwrap.TextWrapper(width=200)
        dedent_news = textwrap.dedent(text=news.text)
        news = wrap.fill(text=dedent_news).strip() + '\n'
        print(news)
