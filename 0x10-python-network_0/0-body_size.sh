#!/bin/bash
# print the byte
curl -I "$1" | grep -w 'Content-Length' | cut -f2 -d' '
