import requests
from bs4 import BeautifulSoup

'''
reuqests --> allows the download html from a website
beautifulsoup --> allows to use html and grap different data and use the gathered data
'''

res = requests.get('https://news.ycombinator.com/news')
#print(res)
#print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')
print(soup)
# prints the the webpage in html format
print(soup.body)
# prints the body
print(soup.body.contents)
# prints the content of the body in a list form
print(soup.find_all('div'))
# prints all the contents with div tags
print(soup.find_all('a'))
# prints all the a tags or the links on the page
print(soup.title)
# prints the title of the soup
print(soup.a)
# prints the first a tag
print(soup.find('a'))
# prints the first a tag
print(soup.find(id='score_20514755'))
# prints the content having the above score
print(soup.select('a'))
# prints all the a tags
print(soup.select('.score'))
#prints all the score contents
print(soup.select('#score_26216016'))
# prints this score content. alwassys use #while searching like this
links = soup.select('.storylink')
votes = soup.select('.score')
print(votes[0])
# prints the first vote