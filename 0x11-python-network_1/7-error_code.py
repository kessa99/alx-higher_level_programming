#!/usr/bin/python3
"""
If the HTTP status code is greater
than or equal to 400, print: Error code:
followed by the value of the HTTP status code
You must use the packages requests and sys
You are not allowed to import packages
other than requests and sys
You don’t need to check arguments
passed to the script (number or type)
"""

import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code:", r.status_code)
    else:
        print(r.text)
