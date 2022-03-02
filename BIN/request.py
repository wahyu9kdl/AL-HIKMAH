#!/usr/bin/python
# -*- coding: utf-8 -*-
# Works on python 3 and python 2.
# when server knows where the request is coming from.

import sys

if sys.version_info[0] == 3:
    from urllib.request import urlopen
else:
    from urllib import urlopen
with urlopen('https://www.alhikmah.my.id/') as \
    url:
    data = url.read()

print data

# When the server does not know where the request is coming from.
# Works on python 3.

import urllib.request

user_agent = \
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

url = 'https://www.alhikmah.my.id/'
headers = {'User-Agent': user_agent}

request = urllib.request.Request(url, None, headers)
response = urllib.request.urlopen(request)
data = response.read()
print data
