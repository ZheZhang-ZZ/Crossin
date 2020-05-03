import random
symbol = ['♦','♣','♥','♠']
num = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
poker = [y+x for x in num for y in symbol]
poker.extend(['joker','JOKER'])
#print(poker)

def list_remov(remov,lst):
  for i in remov:
    lst.remove(i)
  return None

poker2 = poker
a=random.sample(poker2,17)
list_remov(a,poker2)
b=random.sample(poker2,17)
list_remov(b,poker2)
c=random.sample(poker2,17)
list_remov(c,poker2)
d=poker2

print(a)
print(b)
print(c)
print(d)
