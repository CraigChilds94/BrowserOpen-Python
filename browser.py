#!/usr/bin/env python
import sys, os
args = sys.argv
file_url = args[1] if args[1] else "index.html"
os.system("open " + file_url)
for a in ["safari", "firefox", "opera"]:
	os.system("open -a " + a + " " + file_url)