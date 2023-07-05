#!/usr/bin/python3
"""
You must use the packages urllib and sys
You are not allow to import
packages other than urllib and sys
The value of this variable is
different for each request
You don’t need to check arguments
passed to the script (number or type)
You must use a with statement
"""

import sys
import urllib.request

url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    head = response.getheaders()

for response in head:
    if response[0] == 'X-Request-Id':
        print(response[1])
