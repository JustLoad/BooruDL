import requests
from bs4 import BeautifulSoup
import sys


link = sys.argv[1]
r = requests.get(link)

soup = BeautifulSoup(r.text, 'html.parser')
res = soup.find_all("img")

if link.startswith("https://danbooru.donmai.us/"):
    r2 = requests.get(res[0]["src"])
    open("result.png", "wb").write(r2.content)

elif link.startswith("https://yande.re"):
    r2 = requests.get(res[1]["src"])
    open("result.png", "wb").write(r2.content)

elif link.startswith("https://safebooru.org/"):
    r2 = requests.get(res[2]["src"])
    open("result.png", "wb").write(r2.content)
