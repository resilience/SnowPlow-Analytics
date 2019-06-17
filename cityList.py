

from urllib.request import FancyURLopener
import urllib, json

# -------- init 

mz = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
apple = ' AppleWebKit/537.36 (KHTML, like Gecko) '
chrome = 'Chrome/66.0.3359.181 Safari/537.36'

class MyOpener(FancyURLopener): version = mz + apple + chrome

myopener = MyOpener()


this = 'http://jsonplaceholder.typicode.com/users'

JSONSearch = myopener.open(this.strip()).read()

infoblob = json.loads(JSONSearch.decode('utf-8'))



for userInfo in infoblob:
    #print('user: ', userInfo)
    city = userInfo['address'].get('city')
    print(city)
