#!/usr/bin/env python
import sys, os
for a in ["default", "safari", "firefox", "opera"]: os.system("open" + (" -a " + a if a != "default" else "") + " " + (sys.argv[1] if sys.argv[1] else "index.html"))