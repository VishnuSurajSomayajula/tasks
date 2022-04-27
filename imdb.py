"""...Task 27- WEB scrapping IMDB website..."""

import requests
import pandas as pd
from bs4 import BeautifulSoup

response = requests.get('https://www.imdb.com/chart/top/')
# print (response) # 200 response received
soup = BeautifulSoup(response.content, 'html.parser')
# print (soup)
names = soup.find_all('td', class_='titleColumn')
# print (names)
name = []
for i in range(0, len(names)):
    name.append(names[i].a.get_text())
# print (name)
years = soup.find_all('td', class_='titleColumn')
# print(years)
year = []
for i in range(0, len(years)):
    year.append(years[i].span.get_text())
# print(year)

ratings = soup.find_all('td', class_='ratingColumn imdbRating')
# print (ratings)
ratings1 = []
for i in range(0, len(ratings)):
    ratings1.append(ratings[i].strong.get_text())
# print(ratings1)


images = soup.find_all('td', class_="posterColumn")
# print(images)
image = []

for i in range(0, len(images)):
    image.append(images[i].a.img['src'])
# print(image)

links = soup.find_all('td', class_='titleColumn')

# print(links)
link = []

for i in range(0, len(links)):
    d = "https://www.imdb.com" + links[1].a['href']
    link.append(d)
# print(link)

df = pd.DataFrame()
# Creating Data Frame
df['Movie Name: '] = name
df['Year Released: '] = year
df['Movie Rating: '] = ratings1
df['Images: '] = image
df['links:  '] = link
#df.to_csv('Imdb top movies.csv')

