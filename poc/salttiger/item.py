from bs4 import BeautifulSoup
import requests
import re
from record import Record

detail_url = 'https://salttiger.com/modern-data-architecture-on-aws/'
# detail_url = 'https://salttiger.com/training-data-for-machine-learning/'
web_data = requests.get(detail_url)
soup = BeautifulSoup(web_data.content, 'html.parser')

title = soup.select_one('h1.entry-title').text
print(f'title = {title}')

cover_image_url = soup.select_one('.alignnone')['src']
print(f'cover_image_url = {cover_image_url}')

element_book_info = soup.select_one('strong')

element_links = element_book_info.select('a')
element_link_press = element_links[0]
press_name = element_link_press.text
press_book_url = element_link_press['href']

print(f'press_name = {press_name}')
print(f'press_book_url = {press_book_url}')

element_link_baidu_pan = element_links[1]
baidu_pan_url = element_link_baidu_pan['href']

print(f'baidu_pan_url = {baidu_pan_url}')

element_contents = soup.select('.entry-content p')[1:]
for line in element_contents:
    print(line.text)
