import requests
import time
from urllib.request import urlretrieve
from bs4 import BeautifulSoup as BS
from requests.packages.urllib3.connectionpool import HTTPConnectionPool
from requests.adapters import HTTPAdapter
import time
import socks
import socket
import xlwt
from urllib3.util.retry import Retry
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
s = requests.Session()
retries = Retry(total=5,
                backoff_factor=2,
                status_forcelist=[503])
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
f = open('this_path_delete',encoding='UTF8')
itt=1
masnameall=[]
ittcharsnames=0
for line in f:
    masnameall=[]
    itt+=1
    checkIP()
    findname=0
    print('opened')
    article = line.replace("\n", "")
    s.mount(f"https://www.etm.ru/cat/nn/{id}", HTTPAdapter(max_retries=retries))
    r = s.get('https://www.etm.ru/cat/nn/'+article,headers=headers,verify=False)
    html = BS(r.content, 'html.parser')
    print(article)
    for el in html.select('div.breadcrumbs a'):
        name = el
        print(name.text)
        masnameall.append(name.text)
    print(masnameall)
    item_i=0
    sheet1.write(itt, 0, article)
    while item_i < len(masnameall):
        item_i+=1
        print(f'itt = {itt} stroka = {item_i} text = {name.text}')
        sheet1.write(itt, item_i, name.text)
    book.save("etmru_categories.xls")