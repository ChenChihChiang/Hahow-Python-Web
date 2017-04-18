import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

headers = {
	
	'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
}
res =requests.get('https://www.ptt.cc/bbs/Beauty/M.1382181195.A.FC8.html', headers=headers)

#print(res.text)

soup = BeautifulSoup(res.text, 'html.parser')

images = soup.select('a[href^=http://i.imgur]')

#print (images)

for image in images:
	#print (image['href'])
	filename = image['href'].split('/')[3]
	print (filename)
	img = urlopen(image['href'])
	with open('./images/'+ str(filename), 'wb') as f:
		f.write(img.read())
