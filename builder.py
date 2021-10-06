import json
import os

# loading templates and locations' JSON
with open("locations.json") as f:
    loc = json.load(f)
with open("templates/location-template.txt") as f:
    lt = f.read()
with open("templates/server-template.txt") as f:
    st = f.read()
with open("templates/index-template.txt") as f:
    wt = f.read()
with open("templates/button-template.txt") as f:
    bt = f.read()

# LOCATIONS
ls = ""
for l in loc["locations"]:
    temp = ""
    for line in lt.splitlines():
        b = line.find("%(")
        e = line.find(")")
        if b >= 0 and e > b:
            prop = line[b+2:e]
            if prop.lower() in l:
                temp += line.replace(f"%({prop})", l[prop.lower()]) + "\n"
        elif b < 0:
            temp += line + "\n"
    for prop in l:
        temp = temp.replace(f"$({prop.upper()})", l[prop])
    ls += temp

# SERVER
ss = ""
temp = st
for prop in loc:
    if type(loc[prop]) == type(str()):
        temp = temp.replace(f"$({prop.upper()})", loc[prop])
ss += temp

# BUTTONS
bs = ""
for l in loc["locations"]:
    temp = bt
    for prop in l:
        temp = temp.replace(f"$({prop.upper()})", l[prop])
    bs += temp

# INDEX
ws = ""
temp = wt
for prop in loc:
    if type(loc[prop]) == type(str()):
        temp = temp.replace(f"$({prop.upper()})", loc[prop])
ws += temp

# Merging LOCATION+SERVER
ss = ss.replace("$(LOCATIONS)", ls)
filename = f"conf/{loc['name']}-proxy.conf"
with open(filename, "w") as f:
    f.write(ss)

# Merging BUTTONS+INDEX
ws = ws.replace("$(BUTTONS)", bs)
with open("www/index.html", "w") as f:
    f.write(ws)
