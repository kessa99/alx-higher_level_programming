#!/usr/bin/python3
"""
You must use the package urllib
You are not allowed to import any
packages other than urllib
The body of the response must be
displayed like the following example (tabulation before -)
You must use a with statement
"""
import urllib.request
url = "https://alx-intranet.hbtn.io/status"
with urllib.request.urlopen(url) as response:
    body = response.read()
    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
    print("\t- utf8 content:", body.decode('utf-8'))
