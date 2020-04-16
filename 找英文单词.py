import re
res=[]
with open('from.txt') as f:
  for line in f:
    line = line.strip()
    m = re.findall(r'[a-zA-z]+', line)
    res.extend(m)
f.close()

res.sort()
with open('to.txt','w') as f:
  for item in res:
    f.write(item+'\n')
f.close()