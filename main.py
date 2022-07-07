import requests
import requests as rq
from bs4 import BeautifulSoup as bs

gitUser = input('Input github username: ')
url = 'https://github.com/' + gitUser

r = requests.get(url)
soup = bs(r.content, 'html.parser')

profileImage = soup.find('img', {'alt': 'Avatar'})['src']
print(profileImage)