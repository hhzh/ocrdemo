import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='scmd', charset='utf8')
# conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='nile', charset='utf8')
# conn = pymysql.connect('localhost','3306' 'root', '1234', 'nile')
cursor = conn.cursor()
# cursor.execute('select * from author where id=1')
# values = cursor.fetchone()
# print(values)
# conn.close()

resultTXT = ''
with open(r'E:\github\ocrdemo\img\img\8799389f35fe2f23f8f6e75499da1dd3\result.txt', 'r',encoding='utf-8') as fp:
    for line in fp.readlines():
        resultTXT = resultTXT + line

sql = 'insert into sc_ocr (result,imgMD5) values (%s,%s)'
result = cursor.execute(sql, (resultTXT, '8799389f35fe2f23f8f6e75499da1dd3'))
print(result)
conn.commit()
conn.close()
