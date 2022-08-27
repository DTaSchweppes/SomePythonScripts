import requests
import time
from urllib.request import urlretrieve
from bs4 import BeautifulSoup as BS
from requests.packages.urllib3.connectionpool import HTTPConnectionPool
import time
import socks
import socket
import xlwt
import xlrd
def _make_request(self,conn,method,url,**kwargs):
    response = self._old_make_request(conn,method,url,**kwargs)
    sock = getattr(conn,'sock',False)
    if sock:
        setattr(response,'peer',sock.getpeername())
    else:
        setattr(response,'peer',None)
    return response
def checkIP():
    ip = requests.get('http://checkip.dyndns.org').content
    soup = BS(ip, 'html.parser')
    print(soup.find('body').text)
socks.set_default_proxy(socks.SOCKS5, "localhost", 9150)
socket.socket = socks.socksocket
HTTPConnectionPool._old_make_request = HTTPConnectionPool._make_request
HTTPConnectionPool._make_request = _make_request
import xlwt
book = xlwt.Workbook(encoding="utf-8")
data =xlrd.open_workbook('categorys.xls')
sheet = data.sheet_by_index(0)
sheet1 = book.add_sheet("Sheet 1",cell_overwrite_ok=True) #обязательно создаем лист
sheet2 = book.add_sheet("Sheet 2",cell_overwrite_ok=True) #обязательно создаем лист
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
itt=1
masnameall=[]
ittcharsnames=0
masnameall=[]
checkIP()
findname=0
print('opened')
r = requests.get('https://rdstroy.ru/catalog/knauf_3/',headers=headers,verify=False)
html = BS(r.content, 'html.parser')
list_name =[]
list_price=[]
list_code=[]
for el in html.select('span.price_span'):
    name = el
    print('====')
    print(name.text)
    list_price.append(name.text)
    print('====')
for el in html.select('div.name.item'):
    name = el
    print('====')
    print(name.text)
    list_name.append(name.text)
    print('====')
for el in html.select('p.good_id'):
    name = el
    print("good "+ name.text)
    list_code.append(name.text)
i=0
while i< len(list_code):
    sheet1.write(itt, 0, list_code[i])
    sheet1.write(itt, 1, list_name[i])
    sheet1.write(itt, 2, list_price[i])
    i+=1
    itt+=1
book.save("gips.xls")