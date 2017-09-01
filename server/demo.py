from wsgiref.simple_server import make_server


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']


def application1(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    print(type(environ))
    print(len((environ)))
    print(environ)
    return [body.encode('utf-8')]


httpd = make_server('', 8000, application1)
print('Server Http on port 8000....')
httpd.serve_forever()
