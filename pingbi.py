f=open('pingbi.txt')
lst=f.readlines()

test='啊啊，这是一个测试啊啊啊啊'
for i in lst:
  i.strip('\n')
  print(i)
  star='*'*len(i)
  test.replace(i, star)

print(test)
f.close()
