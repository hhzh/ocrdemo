import requests

# files = {'file': ('imgData', open('d:/git.jpg', 'rb'), 'image/jpeg')}
files = {'file': open('e:/5.jpg', 'rb')}

# response = requests.post('http://www.carecnn.com/upload', files=files)
response = requests.post('http://127.0.0.1:5000/upload', files=files)

print(response.status_code)
print(response.text)

# MD5 = ''
# print(type(response.text))
# print(len(response.text))
# print(response.text)
# lines=response.text.splitlines()
# for line in lines:
#     if line.startswith('<h1>MD5'):
#         MD5 = line[line.index('<h1>MD5:') + 8:line.index('</h1>')]
# print(MD5.strip())