#!/bin/bash
#Displays all HTTP methods the server will accept
curl -si -sL -sX OPTIONS "$1"
