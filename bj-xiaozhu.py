import requests
from bs4 import BeautifulSoup
import time
import re


def whoisshe(class_name):
    if class_name == ['member_ico']:
        return '男'
    return '女'


def start():
    url_list = ['http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(i) for i in range(1, gettotalpages() + 1)]
    print(url_list)
    for url in url_list:
        soup = dorequestwithsoup(url, 'html.praser')
        links = soup.select('#page_list > ul > li > a')
        # print(links)
        for link in links:
            # print(link.get('href'))
            getinfo(link.get('href'))
            time.sleep(2)


def getinfo(data_url):
    soup = dorequestwithsoup(data_url, 'html.praser')
    titles = soup.select('body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > h4 > em')
    addresses = soup.select('body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > p > span')
    prices = soup.select('#pricePart > div.day_l > span')
    names = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')
    sexs = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > div')
    imgs = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > a > img')  # src
    for title, address, price, name, sex, img in zip(titles, addresses, prices, names, sexs, imgs):
        doprint(title.text, address.text, price.text, name.text, whoisshe(sex.get('class')), img.get('src'))


# 标题、地址、价格、房东名称、房东性别和房东头像
def doprint(title, address, price, name, sex, img):
    print('House[title=' + str(title) + ', address=' + str(address) \
          + ', price=' + str(price) + ', name=' + str(name) + ', sex=' \
          + str(sex) + ', img=' + str(img) + ', ]')


def gettotalpages():
    url = 'http://bj.xiaozhu.com/'
    soup = dorequestwithsoup(url, 'html.praser')
    pagelist = soup.select('#totalPages')
    if len(pagelist) == 0:
        raise RuntimeError('cannot found totalpages')

    return int(pagelist[0].get('value'))


def dorequestwithsoup(url, parser):
    parsers = {
        'html.praser': True,
        'lxml': True,
        '["lxml,xml"]': True,
        'xml': True,
        'html5lib': True
    }
    if not parsers.get(parser, False):
        raise RuntimeError('Invalid parser[' + str(parser) + '] in parsers[' + str(parsers) + ']')

    res = dorequest(url)
    if res.status_code != 200:
        raise RuntimeError('Error response status_code, response:'+str(res))

    return BeautifulSoup(res.text, 'html.parser')


def dorequest(url):
    if not isinstance(url, str) or url.strip() == '':
        raise RuntimeError('Invalid request url['+str(url)+']')

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                      ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
    }
    res = requests.get(url.strip(), headers=headers)
    if res.status_code != 200:
        raise RuntimeError('Error response status_code, response:'+str(res))

    return res


if __name__ == '__main__':
    # start()
    res = dorequest('http://bj.xiaozhu.com/')
    # print(res.text)
    prices = re.findall('<span class="result_price">&#165;<i>(.*?)</i>起/晚</span>', res.text)
    print(prices)
