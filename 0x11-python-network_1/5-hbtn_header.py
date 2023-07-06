#!/usr/bin/python3
"""
You must use the packages requests and sys
You are not allow to import
other packages than requests and sys
The value of this variable is
different for each request
You don’t need to check script
arguments (number and type)
"""

import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    r = requests.get(url)
    print(r.headers['X-Request-Id'])
