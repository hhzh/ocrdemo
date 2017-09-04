import request_pb2
import socket
import pickle

result = '我来到北京清华大学。'

request = request_pb2.Request()
request.request_buf = result.encode('utf-8')
request.userId = 32
request.imgMD5 = '95083e7bca6b09fb4c02e7cd666ab506'

request_str = 'QSBEAACA' + str(len(result.encode('gbk'))) + '\t' + result + 'QS55AACA'
ip_port = ('127.0.0.1', 10001)
# ip_port = ('114.112.104.150', 10001)
web = socket.socket()

web.connect(ip_port)
# web.sendall(request)
web.sendall(bytes(request_str, 'utf-8'))
server_reply = web.recv(1024)
print(type(server_reply))
print(server_reply)
print(str(server_reply, 'utf-8'))
web.close()

# xx = pickle.dumps(request)
# # xx = pickle.dump(request, open('res.txt', 'wb'))
# print(type(xx))
# print(xx)
# with open('res.txt','rb') as fp:
#     for line in fp.readlines():
#         print(line)
# dd=pickle.load(open('res.txt','rb'))
# print(type(dd))
# print(dd)