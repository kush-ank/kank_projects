import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
#print(res)
#print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
#votes = soup.select('.score')
subtext = soup.select('.subtext')


def sort_stories_by_votes(hnlist):
	return sorted(hnlist, key = lambda k:k['votes'], reverse=True)


def create_custom_hn(links, subtext):
	hn = []
	for idx, item in enumerate(links):
		title = item.getText()
		href = item.get('href', None)
		votes = subtext[idx].select('.score')
		if len(votes):
			points = int(votes[0].getText().replace(' points',''))
#			print(points)
			if points > 99:
				hn.append({'title': title, 'link': href, 'votes': points})
	return hn

pprint.pprint(create_custom_hn(links, subtext))

'''
enumerate gets the index from the links and based on the index the related value is
fethced from the subtext. Since both are lists, to relate the two lists:- links and
subtext, we have to enumerate the index from one list and provide it to another.
'''

'''
pprint --> pretty print
helps to print the data neatly in the command terminal
'''

'''
while sorting a dictionary, use lambda and based on a key; here its votes, sort the
data in the dictionary. If needed based on any other field the key needs to be 
changed accordingly.
	return sorted(hnlist, key = lambda k:k['votes'], reverse=True)
reverse is needed if you need the highest value at the top and lowest at the bottom
'''