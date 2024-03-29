#!/usr/bin/python3
"""
ou have to manage urllib.error.HTTPError
exceptions and print: Error code:
followed by the HTTP status code
You must use the packages urllib and sys
You are not allowed to import other
packages than urllib and sys
You don’t need to check arguments
passed to the script (number or type)
You must use the with statement
"""

import urllib.request
import urllib.error
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
