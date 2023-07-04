#!/bin/bash
#script that displays the body response
curl -sI "$1" | grep 'X-School-User-Id:' | cut -d" " -f2-
