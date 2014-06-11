#!/usr/bin/env python
import sys, os

args = sys.argv
file_url = ""

if(args[1]):
	file_url = args[1]
else:
	file_url = "index.html"

os.system("open " + file_url)
os.system("open -a safari " + file_url)
os.system("open -a firefox " + file_url)
os.system("open -a opera " + file_url)