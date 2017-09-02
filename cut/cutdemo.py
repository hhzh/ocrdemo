import cut_pb2
import socket

result = '我来到北京清华大学。'

request_str = 'QSBEAACA' + str(len(result.encode('gbk'))) + '\t' + result + 'QS55AACA'
ip_port = ('114.112.104.150', 10001)
web = socket.socket()

web.connect(ip_port)
web.sendall(bytes(request_str, 'utf-8'))
server_reply = web.recv(1024)
print(str(server_reply, 'utf-8'))
web.close()
