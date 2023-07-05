#!/usr/bin/python3
"""
The email must be sent in the email variable
You must use the packages urllib and sys
You are not allowed to import
packages other than urllib and sys
You don’t need to check arguments
passed to the script (number or type)
You must use the with statement
"""

import urllib.request
import urllib.parse
import sys
if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode(email)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
