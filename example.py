# variables
a = "hello"
b = "world"
print(a, " ", b + "!")
print(a * 3)
print(a[0], a[0:4], a[-1])

# strings
website = " www.baidu.com/{}  "
print(website.split('.'))
print(website.replace('baidu', 'google'))
print(website.strip())
print(website.format('take-me-fun'))  # www.baidu.com/take-me-fun
url_list = ['http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(i) for i in range(1, 14)]

# int to string, string to int
a = 1
b = '2'
print(str(a))
print(int(b))

# && || !
a and b
a or b
not a

# function
def add(x, y):
    return x + y


def padd(x, y):
    print("{} + {} = {}".format(x, y, x + y))


print('3 + 2 =', add(3, 2))
padd(2, 4)


# if else
def count_login():
    pwd = input('password:')
    if pwd == '12345':
        print('登录成功')
    elif pwd == 'xy6':
        print('login success')
    else:
        print('1234 再来一次')
        count_login()


# count_login()

# for and while
for i in range(1, 11):
    print(i)

i = 1
while i < 11:
    print(i)
    i += 1

# struct
# list []
listA = ['hello', '-', 'world', '!']
print(listA, listA[0], listA[2:])
print(len(listA))

names = ['wang', 'fei', 'fan']
ages = [12, 23, 25]
for name, age in zip(names, ages):
    print('{}\'age is {} '.format(name, age))

# map {key:value}
mapA = {'name': 'Wang Feifan', 'age': '23'}
print(mapA)

# tuple ()
tupleA = (1, 2, 3)
print(tupleA)

# set {}
setA = set([1, 2, 3, 3, 4])
print(setA)
setB = {1, 2, 3, 2, 2}
setB.add(2)
print(setB)  # {1, 2, 3}
setB.pop()
print(setB)  # {2, 3}

# file
# open('./rands.txt')  # FileNotFoundError: [Errno 2] No such file or directory: './rands.txt'
f = open('./hello.txt', 'a+')  # r(read) w(write) a(append) b(binary, 可添加到其他模式中使用) +(r/w, 可添加到其他模式中使用)
print(f.read())
f.write(str(a)+'\n')
f.close()


# Class
class Bike:
    compose = ['frame', 'whell', 'pedal']


import requests
from bs4 import BeautifulSoup


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                  ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
}
res = requests.get('http://bj.xiaozhu.com/', headers=headers)
# print(res)

# try:
#     print(res.text)
# except ConnectionError:
#     print('拒绝连接')

soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.prettify())

# price = soup.select('#page_list > ul > li:nth-of-type(2) > div.result_btm_con.lodgeunitname > span.result_price > i')
# print(price)

prices = soup.select('#page_list > ul > li > div.result_btm_con.lodgeunitname > span.result_price > i')
# print(prices)
for price in prices:
    # print(price)
    # print(price.text)
    print(price.get_text())
