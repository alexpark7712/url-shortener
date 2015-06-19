# coding=utf-8
import re
import urllib2
import json

url_pattern = re.compile(
    r'^(?:http|ftp)s?://'  # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
    r'localhost|'  # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
    r'(?::\d+)?'  # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)


def coroutine(func):
    def start(*arg, **kwargs):
        g = func(*arg, **kwargs)
        g.next()
        return g

    return start


@coroutine
def receiver():
    try:
        while True:
            try:
                value = (yield)
                req = urllib2.Request(
                    'https://www.googleapis.com/urlshortener/v1/url?key=AIzaSyA62lFjToSj8yGRr5KRDrtHTZemAz0tuhQ')
                req.add_header('Content-Type', 'application/json')
                data = json.dumps({'longUrl': value})

                res = urllib2.urlopen(req, data)
                dic = json.load(res)

                print "shorten url is: ", dic['id']
            except Exception, e:
                print e
    finally:
        print 'bye\n'


def is_vaild_url(url):
    if not url_pattern.match(url):
        return False
    else:
        return True


r = receiver()

while True:
    s = raw_input("type url: ")
    if s == 'exit' or s == 'bye':
        break

    if not is_vaild_url(s):
        print "wrong url"
    else:
        r.send(s)

r.close()
