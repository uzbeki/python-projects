import re

with open('savol.txt') as s:
    lines = s.readlines()

# pattern = re.compile(r"^?", re.MULTILINE)

for i in lines:
    line = i.strip()
    if line.find("?") != -1:
        print(line)
