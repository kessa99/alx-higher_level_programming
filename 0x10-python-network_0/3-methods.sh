#!/bin/bash
#Displays all HTTP methods the server will accept
curl -Is "$1" | grep -w 'Allow'
