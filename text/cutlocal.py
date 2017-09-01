import socket
from google.protobuf.internal import decoder


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('114.112.104.150', 10001))

# s.send('我来到北京清华大学。')
s.send('我来到北京清华大学'.encode('utf-8'))

# 接收数据:
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
# 关闭连接:
s.close()

header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的数据写入文件:
# with open('sina.html', 'wb') as f:
#     f.write(html)

print(html)