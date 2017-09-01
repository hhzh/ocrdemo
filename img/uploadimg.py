import sys
import os
from flask import Flask, url_for, render_template, request, url_for, redirect, send_from_directory
# from werkzeug import secure_filename
from werkzeug import security

app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def hello():
    print('hello')
    return 'hello world'


@app.route('/upload', methods=['POST'])
def upload_file():
    print('hello')
    print(request.args['imgKey'])
    imgKey = request.files['imgKey']
    print(imgKey)
    if request.method == 'POST':
        imgKey = request.files['imgKey']
        print(imgKey)
        # imgData = request.files['imgData']
        # print('接受图片')
        # with open('img.jpg', 'wb') as fp:
        #     fp.write(imgData)
        return 'OK'

if __name__ == '__main__':
    app.run()
