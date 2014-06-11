#!/usr/bin/env python
import sys, os
args = sys.argv
file_url = args[1] if args[1] else "index.html"
for a in ["default", "safari", "firefox", "opera"]:
	os.system("open" + (" -a " + a if a != "default" else "") + " " + file_url)