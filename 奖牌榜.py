# -*- coding: utf-8 -*-

class metal:
  def __init__(self,country,gold,silver,copper):
    self.country = country
    self.gold = gold
    self.silver = silver
    self.copper = copper

  def addMetal(self,type,num):
    if(type=='gold'):
      self.gold+=num
    elif(type=='silver'):
      self.silver+=num
    elif(type=='copper'):
      self.copper+=num
    else:
      print("无效的奖牌\n")

  def totMetal(self):
    return(self.gold+self.silver+self.copper)

  def printMetal(self):
    res = "国家：%s\t金牌：%d\t银牌：%d\t铜牌：%d\t总奖牌数：%d" \
      % (self.country, self.gold, self.silver, self.copper, self.totMetal())
    return(res)

china = metal('中国',51,102,278)
usa = metal('美国',68,78,156)
russia = metal('俄罗斯',47,165,103)
japan = metal('日本',36,55,98)

board = {}
board['中国'] = china.printMetal()
board['美国'] =usa.printMetal()
board['俄罗斯'] =russia.printMetal()
board['日本'] =japan.printMetal()

tot = {'中国':china.totMetal(), '美国':usa.totMetal(), 
       '俄罗斯':russia.totMetal(), '日本':japan.totMetal()}
tot_country = [k for k, v in sorted(tot.items(), key=lambda item: item[1], reverse=True)]
print("总奖牌榜：")
for country in tot_country:
  print(board[country])

gold = {'中国':china.gold, '美国':usa.gold, 
       '俄罗斯':russia.gold, '日本':japan.gold}
gold_country = [k for k, v in sorted(gold.items(), key=lambda item: item[1], reverse=True)]
print("\n金牌榜：")
for country in gold_country:
  print(board[country])


