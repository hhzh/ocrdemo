from aip import AipOcr
import base64

APP_ID = '9999224'
API_KEY = 'eqDDM65ekpMTxGGXlM658Tvd'
SECRET_KEY = 'BzUyA3S0IoqAmTBd0jGtZ0ghiIzB7dLi'


# 读取图片
def get_file_content(filepath):
    with open(filepath, 'rb') as fp:
        return fp.read()


# 初始化ApiOcr对象
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# 调用通用文字识别接口
result = aipOcr.basicGeneral(get_file_content('e:/1.jpg'))

# 如果图片是url 调用示例如下
# result = aipOcr.basicGeneral('http://img0.ph.126.net/JgZPujjerZ1A7U_6gfs8Ag==/2515260391903843500.jpg')
# result = aipOcr.basicGeneral('https://img1.doubanio.com/lpic/s9155608.jpg')

# print(type(result))
# print(result)
# print(result['words_result'])
for obj in result['words_result']:
    print(obj['words'])
