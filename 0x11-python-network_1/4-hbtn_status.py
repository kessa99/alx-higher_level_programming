#!/usr/bin/python3
"""
You must use the package requests
You are not allow to import
packages other than requests
The body of the response must be
display like the following example (tabulation before -)
"""

if __name__ == '__main__':
    import requests

    url = 'https://alx-intranet.hbtn.io/status'
    r = requests.get(url)
    print("Body response:")
    print("\t- type:", type(r.text))
    print("\t- content:", r.text)
