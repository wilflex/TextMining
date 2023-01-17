
import requests
import bs4 as BeautifulSoup	
import re

url = "https://www.youtube.com/watch?v=0WfcgfGTMlY&list=PLtzmb84AoqRSmv5o-eFNb3i9z64IuOjdX&index=11"
link = "https://www.youtube.com/playlist?list=PLtzmb84AoqRSmv5o-eFNb3i9z64IuOjdX"

#parse link
#try:
    #page = requests.get(link)
    #soup = BeautifulSoup.BeautifulSoup(page.text,"lxml")
    #for element in soup.find_all("div",id="container"):
        #div = element.find("h3",class_="style-scope ytd-playlist-video-renderer")
        #title = div.find("a").text
        #print(title)


#except Exception as e:
    #print(e)


headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
                      }
page = requests.get(link,headers)
soup = BeautifulSoup.BeautifulSoup(page.text)
for element in soup.find_all("div",id="container"):
    div = element.find("h3",class_="style-scope ytd-playlist-video-renderer")
    title = div.find("a")
    print(title.text)