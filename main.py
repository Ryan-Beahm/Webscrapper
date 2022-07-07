#freecodecamp project
import requests as rq
from bs4 import BeautifulSoup as bs

gitUser = input('Input github username: ')
url = 'https://github.com/' + gitUser

# r stores the return code 200 and r.content stores the html file for further sorting
r = rq.get(url)
# test
# print(r.content)

# usable data formatting
# print(bs(r.content, 'html.parser'))
soup = bs(r.content, 'html.parser')

# tag filtering
profileImage = soup.find('img', {'alt': 'Avatar'})['src']
print(profileImage)
