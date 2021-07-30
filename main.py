URL = "https://www.empireonline.com/movies/features/best-movies-2"

import requests
from bs4 import BeautifulSoup

response = requests.get(URL)

soup = BeautifulSoup(response.text, 'html.parser')

results = soup.find_all(name="h3")

print(results)