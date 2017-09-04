import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='nile', charset='utf8')
# conn = pymysql.connect('localhost','3306' 'root', '1234', 'nile')
cursor = conn.cursor()
# cursor.execute('select * from author where id=1')
# values = cursor.fetchone()
# print(values)
# conn.close()

sql = 'insert into author (name,profile) values (%s,"one author")'
result = cursor.execute(sql, ('莫言'))
print(result)
conn.commit()
conn.close()
