# -*- coding: utf-8 -*-

def sum_line(a):
  sum = 0
  for i in a:
    sum+=int(i)
  return sum

def mean(a):
  return round(sum_line(a)/len(a),1)

f = open("score.txt")

res=[]
average={}
header = []
cnt = 0

for line in f:
  line = line.strip()

  if not line.startswith("姓名"):
    cnt+=1
    line = line.split(" ")
    i=0
    ind=[line[0]]
    for score in line[1:]:
      average[header[i]]+=int(score)
      i+=1
      if(int(score)<60):
        ind.append('不及格')
      else:
        ind.append(int(score))
    ind.append(sum_line(line[1:]))
    ind.append(mean(line[1:]))
    res.append(ind)
  else:
    line = line.split(" ")
    for item in line[1:]:
      header.append(item)
      average[item] = 0

f.close()

firstline=[0,'平均']
firstline_sum=0
for head in header:
  temp=round(average[head]/float(cnt))
  firstline.append(temp)
  firstline_sum+=temp
firstline_mean=round(firstline_sum/len(header),1)
firstline.extend([firstline_sum,firstline_mean])

firstline=[str(x) for x in firstline]
firstline=" ".join(firstline)
header.extend(['总分','平均分'])
header.insert(0,'科目')
header.insert(0,'名次')
header=" ".join(header)

res = sorted(res, key=lambda x: -x[-1])

f = open("result.txt",'w')
f.write(header+"\n")
f.write(firstline+"\n")

i=1
for person in res:
  person=[str(x) for x in person]
  person = " ".join(person)
  f.write(str(i)+" "+person+"\n")
  i+=1

f.close()