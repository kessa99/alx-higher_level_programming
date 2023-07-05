#!/usr/bin/python3
import sys
import urllib.request
url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    head = response.getheaders()

for response in head:
    if response[0] == 'X-Request-Id':
        print(response[1])
