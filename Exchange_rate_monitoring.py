from bs4 import BeautifulSoup
from urllib import request
from urllib import parse
import time
import send_email as send
from tqdm import tqdm

url = "https://srh.bankofchina.com/search/whpj/search_cn.jsp"
Form_Data = {}
Form_Data['erectDate'] = ''
Form_Data['nothing'] = ''
aus = 500
bri = 1000
cnt = 0
while True:
    cnt = cnt+1
    try:
        Form_Data['pjname'] = '加拿大元'
        data = parse.urlencode(Form_Data).encode('utf-8')
        html = request.urlopen(url,data).read()
        from datetime import datetime
        current_date_and_time = datetime.now()
        soup = BeautifulSoup(html,'html.parser')
        div = soup.find('div', attrs = {'class':'BOC_main publish'})
        table = div.find('table')
        # print(type(table))
        tr = table.find_all('tr')
        td = tr[1].find_all('td')
        msg = f'{current_date_and_time: }' + 'Canadian Dollar '+td[-1].get_text()+" "+td[3].get_text()

        print(msg)


        Form_Data['pjname'] = '美元'
        data = parse.urlencode(Form_Data).encode('utf-8')
        html = request.urlopen(url,data).read()
        soup = BeautifulSoup(html,'html.parser')
        div = soup.find('div', attrs = {'class':'BOC_main publish'})
        table = div.find('table')
        # print(type(table))
        tr = table.find_all('tr')
        td = tr[1].find_all('td')
        
        msg = f'{current_date_and_time: }' + 'US Dollar  '+td[-1].get_text()+" "+td[3].get_text()
        print(msg)
        time.sleep(60)

    except Exception as e:
        print(e)
        time.sleep(30)
        continue
