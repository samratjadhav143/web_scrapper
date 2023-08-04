# import requests
# from bs4 import BeautifulSoup as bs
# from urllib.request import urlopen as uReq
# import logging

# flipcart_url = 'https://www.flipkart.com/search?q=' + 'iphone12pro'

# urlclient = uReq(flipcart_url)

# flipcart_page = urlclient.read()

# flipcart_html = bs(flipcart_page,'html.parser')
# bigbox = flipcart_html.find_all("div", {"class": "_1AtVbE col-12-12"})

# # print(len(bigbox))
# # print(div.div.div.a['href'])
# del bigbox[0:2]

# for i in (len(bigbox)):
#     print("https://www.flipkart.com"+ i.div.div.div.a['href'])

# import requests
# from bs4 import BeautifulSoup as bs
# from urllib.request import urlopen
# import logging

# flipcart_url= "https://www.flipkart.com/search?q="+"iphone12pro"

# urlClient=urlopen(flipcart_url)

# flipcart_page=urlClient.read()

# flipcart_html=bs(flipcart_page,'html.parser')

# bigbox=flipcart_html.findAll("div",{"class": "_1AtVbE col-12-12"})
# print(len(bigbox))

# del bigbox[0:2]
# del bigbox[-3]

# for i in bigbox:


import requests
from bs4 import BeautifulSoup as bs 
from urllib.request import urlopen
import logging

flipcart_url = "https://www.flipkart.com/search?q=" + "iphone12pro"

urlclint = urlopen(flipcart_url)

flipcart_url = urlclint.read()

flipcart_html= bs(flipcart_url,'html.parser')

bigbox = flipcart_html.findAll("div",{"class":"_1AtVbE col-12-12"})
print(len(bigbox))
del bigbox[0:2]
del bigbox[-3:]

for i in range(len(bigbox)):
    print(bigbox[i].div.div.div.a['href'])


print(len(bigbox))