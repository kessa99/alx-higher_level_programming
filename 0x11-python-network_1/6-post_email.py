#!/usr/bin/python3
"""
The email must be sent in the variable email
You must use the packages
requests and sys
You are not allowed to import packages
other than requests and sys
You don’t need to error check arguments
passed to the script (number or type)
"""

import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    r = requests.post(url, data=data)
    print(r.text)
