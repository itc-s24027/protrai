# s24027
# 沖縄県の推計人口のページより最新情報をスクレイピングするPythonコード
# https://www.pref.okinawa.jp/toukeika/estimates/estimates_suikei.html

import requests
from bs4 import BeautifulSoup

uri = 'https://www.pref.okinawa.jp/toukeika/estimates/estimates_suikei.html'
html = requests.get(uri)

#　文字コード
html.encoding = 'shift_JIS'
#print(html.text)

soup = BeautifulSoup(html.text, 'html.parser')
print(soup.find('title').string)

backnumber = soup.find('table', class_='table1 font2 gyo5')
#print(backnumber)

a = []

for element in backnumber('td', align="right"):
    a.append(element)

    #print(a)


print(f"総人口:{a[0]}人")
print(f"男:{a[1]}人")
print(f"女:{a[2]}人")
