import requests
import pymysql
import json

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='SCMD_2017_scmd', db='douban',
                       charset='utf8')
cursor = conn.cursor()

num = 9979
# while num < 9960:
data = {'sort': 'T', 'range': '0,10', 'start': num}
response = requests.post('https://movie.douban.com/j/new_search_subjects', data=data)
# num += 20

result = json.loads(response.text)
data_result = result['data']
for data_obj in data_result:
    id = int(data_obj['id'])
    title = data_obj['title']
    rate = float(data_obj['rate'])
    star = int(data_obj['star'])
    url = data_obj['url']
    casts = '/'.join(data_obj['casts'])
    directors = '/'.join(data_obj['directors'])
    cover = data_obj['cover']
    cover_x = data_obj['cover_x']
    cover_y = data_obj['cover_y']

    try:
        sql = 'insert into film (id,title,rate,star,url,casts,directors,cover,cover_x,cover_y) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        exec_result = cursor.execute(sql, (id, title, rate, star, url, casts, directors, cover, cover_x, cover_y))
        conn.commit()
        print(num, exec_result, id)
    except Exception as e:
        print(e)

conn.close()
