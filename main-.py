import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)
response_text = response.text

soup = BeautifulSoup(response_text, parser="html.parser", features="lxml")

movie_names = soup.find_all(name="h3", class_="title")

newlist = [movie_name.string for movie_name in movie_names]

newlist.reverse()

print(newlist)

with open(file="movies.txt", mode="w", encoding="utf-8") as file:
    for item in newlist:
        file.write(item + "\n")
