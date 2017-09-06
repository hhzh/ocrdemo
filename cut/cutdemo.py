import ocrrequest_pb2
import socket
import pickle

result = '我来到北京清华大学。'

request = ocrrequest_pb2.Request()
request.Request_buf = result.encode('gbk')
request.UserId = 32
request.imgMD5 = '95083e7bca6b09fb4c02e7cd666ab506'.encode('gbk')

data = request.SerializeToString()
xhead = '\t' + 'QS55AACA'
xlen = str(len(xhead) + len(str(data))).zfill(8)
# xlen = str(140).zfill(8)
request_str = 'QSEpsL01QSBEAACA' + xlen + '\t' + str(data) + 'QS55AACA'

# print(type(data))
# print(type(request_str))
# print('---')
# print(type(xlen))
# print(xlen)
print(request_str)
# print(bytes(request_str, 'gbk'))

# print(len(data))
# print(data)
# print(str(data))
# print(len(str(data)))
# print(len(xhead))


# ip_port = ('127.0.0.1', 10001)
ip_port = ('114.112.104.150', 10001)
web = socket.socket()

web.connect(ip_port)
web.sendall(bytes(request_str, 'gbk'))
server_reply = web.recv(1024)
print(type(server_reply))
print(server_reply)
print(str(server_reply, 'gbk'))
print(server_reply.decode('gbk'))
web.close()

# xx = pickle.dumps(request)
# xx = pickle.dump(request, open('res.txt', 'wb'))
# print(type(xx))
# print(xx)
# with open('res.txt','rb') as fp:
#     for line in fp.readlines():
#         print(line)
# dd=pickle.load(open('res.txt','rb'))
# print(type(dd))
# print(dd)
