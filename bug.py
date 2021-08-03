#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests
from lxml import etree
import random
a = input('请输入次数:')
b=int(a)  #转换类型
if b >3000:
  print('请输入小于3000的值')
else:  
 for i in range (b):
  p=random.randint(0,10000)
  url = 'https://so.niostack.com/search?q=inurl:php?id='+str(p)+'%E5%85%AC%E5%8F%B8'  #拼接批量遍历
#print(url)
  html = requests.get(url)  # 打开网站
#print(html.text)
  text = html.content.decode('utf-8')  #转文本
#print(text)
  open = etree.HTML(text)
  ul = open.xpath('//div/div[@class="external-link"]')  #xpath提取
#print(ul)
  for index in range(len(ul)):
    # links[index]返回的是一个字典
      if (index % 2) == 0:
          x=(ul[index].text)
          y=(ul[index].text)
          z=(ul[index].text)
  print(x)

print('执行结束')  
