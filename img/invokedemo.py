import requests

# result = requests.get('http://127.0.0.1:5000/hello')
# print(result)
# print(result.text)
# # bycon = ''
# # with open(r'D:\demo\4_linxuewei_linbaliu\20110505_xuechanggui\1img.jpg', mode='rb') as fp:
# #     bycon = str(fp.read())
# cont = {'imgKey': 'sodjfwoej'}
# result = requests.post(url='http://127.0.0.1:5000/upload', data=cont)
# print(result.text)

response = requests.get('http://www.carecnn.com/fbd7cbac902536f39cd9ca341fddbee1')
print(response.status_code)
with open('md5.jpg', 'wb') as fp:
    fp.write(response.content)
