BrowserOpen-Python
==================

This is a small python script for MacOSX which opens a given url in the default browser, safari, firefox and opera.

How to run:

```
cd path/to/browser.py
python browser.py http://google.co.uk
```

Or if you want to open ```index.html``` in the same ```dir``` as ```browser.py``` you can leave out the argument:

```
cd path/to/browser.py
python browser.py
```

####Running from anywhere

First copy the ```browser.py``` file into your bin folder, for mac:

```
cp path/to/download/of/browser.py ~/bin/
```

Then make it executable:

```
cd ~/bin/
chmod +x browser.py
```

You should now be able to run (from any directory):

```
browser.py http://google.co.uk
```