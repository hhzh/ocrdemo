import requests
import pymysql
import json



data = {'sort': 'T', 'range': '0,10', 'start': num}
response = requests.post('https://movie.douban.com/j/new_search_subjects', data=data)