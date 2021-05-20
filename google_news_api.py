from GoogleNews import GoogleNews
import random

def GNews():
    gn = GoogleNews()
    gn.set_period('7d')
    list = ["INDIA","USA","UK","AUSTRALIA","FRANC","UGANDA","PAKISTAN","MALDIVES","CELEBRITY"]
    
    gn.search(random.choice(list))
    rs = gn.results()
    
    for i in rs:
      data = i['title']
      data += i['desc']
      data += i['link']
    return data    
