#!/usr/bin/python3

import re
cnt=0
with open('from.txt') as f:
  for line in f:
    line = line.strip()
    m = re.findall(r'[a-zA-z]+', line)
    cnt+=len(m)
f.close()
print("There are %d words in words.txt\n" % cnt)
