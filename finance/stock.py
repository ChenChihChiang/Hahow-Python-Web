import requests
from bs4 import BeautifulSoup
import pandas as pd
import time 

url = 'http://www.twse.com.tw/ch/trading/exchange/BWIBBU/BWIBBU.php'


def parserTSE(year, month, no):
	year = str(year)
	month = str(month)
	no = str(no)

	payload = {
		'query_year': year,
		'query_month': month,
		'CO_ID': no,
		'query-button':'%E6%9F%A5%E8%A9%A2'
	}

	headers = {
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
	}

	res = requests.post(url, headers=headers, data=payload)
	#data = res.text.encode('latin1').decode('big5')
	#print (res.text)
	soup = BeautifulSoup(res.text, 'html.parser')

	#cpntent = soup.select('.board')
	content = soup.find_all('table')[0]

	with open ('./' + year + month + '_tst_' + no + '.html', 'w') as f:
		f.write(str(content))

	table = pd.read_html('./' + year + month + '_tst_' + no + '.html')[0]
 
	print (table.to_csv(header=False, index=False))

	with open('./' + year + '_tse_' + no + '.csv', 'a') as f:
		f.write(str(table.to_csv(header=False, index=False)))


for m in range(1, 13):
	time.sleep(5)
	parserTSE(2015, m, 2317)
