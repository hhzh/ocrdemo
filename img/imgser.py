import requests

# files = {'file': ('imgData', open('d:/git.jpg', 'rb'), 'image/jpeg')}
files = {'file': open('e:/da.png', 'rb')}

response = requests.post('https://www.carecnn.com/upload', files=files)
# response = requests.post('http://114.112.104.150:5000/upload', files=files)
# response = requests.post('http://127.0.0.1:5000/upload?userId=', files=files)
print(type(response))
print(response.status_code)
print(response.text)

# # response = requests.post('http://114.112.104.150:5000/uploadMD5', data={'md5': '8799389f35fe2f23f8f6e75499da1dd3'})
# response = requests.post('http://127.0.0.1:5000/uploadMD5', data={'md5': '8799389f35fe2f23f8f6e75499da1dd3'})
# print(response.status_code)
# print(response.text)

# # response = requests.get('http://114.112.104.150:5000/hello')
# response = requests.get('http://localhost:5000/hello')
# print(response.status_code)
# print(response.text)

# MD5 = ''
# print(type(response.text))
# print(len(response.text))
# print(response.text)
# lines=response.text.splitlines()
# for line in lines:
#     if line.startswith('<h1>MD5'):
#         MD5 = line[line.index('<h1>MD5:') + 8:line.index('</h1>')]
# print(MD5.strip())
