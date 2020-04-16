# -*- coding: utf-8 -*-
import requests
import os

def answer():
  req = requests.get('https://python666.cn/cls/number/guess/')
  content = req.text
  return(int(content))

def read_res():
  res = {}
  if not os.path.exists('./game_res.txt'):
    with open('game_res.txt', 'w'):
      pass
  else:
    with open('game_res.txt') as f:
      for line in f:
        line = line.strip()
        array = line.split()
        res[array[0]] = line
    f.close()
  return res

def game_init(name,info):
  if info.get(name):
    array = info[name].split()
    print("%s，你已经玩了%s次，最少%s轮猜出答案，平均%s轮猜出答案，开始游戏!\n" \
      % (name, array[1], array[2], array[3]))
  else:
    print("%s，你已经玩了%d次，最少%d轮猜出答案，平均%f轮猜出答案，开始游戏!\n" \
      % (name, 0, 0, 0.00))
    info[name] = "\t".join([name,str(0),str(0),str(0.00)])
  return info

class players:
  def __init__(self,name):
    self.name = name
    info = read_res()
    self.info = game_init(name,info)
    self.answer = answer()

name = input("请输入你的名字：")
player = players(name)

numOfRound=0
answer = player.answer
while True:
  try:
    guess = int(input('请猜一个1-100的数字（输入负数强制终止游戏）：'))
  except:
    print("非法输入，必须输入一个整数!\n")
    continue

  if(guess<0):
    print("您强制终止了游戏，本次游戏结果并不计入您的历史!\n")
    break
  elif(guess<1 or guess >100):
    print("无效输入，数字必须在1-100之间\n")
    continue
  else:
    numOfRound+=1
    if(guess>answer):
      print("猜大了，再试试")
    elif(guess<answer):
      print("猜小了，再试试")
    else:
      print("猜对了，你一共猜了%d轮" % numOfRound)
      array = player.info[name]
      array = array.split('\t')
      array[1] = int(array[1])
      array[2] = int(array[2])
      array[3] = float(array[3])
      array[3] = (array[3]*array[1]+numOfRound)/(array[1]+1)
      array[1] += 1
      if not array[2]==0:
        array[2] = min(numOfRound,array[2])
      else:
        array[2] = max(numOfRound,array[2])
      numOfRound = 0
      print("%s，你已经玩了%d次，最少%d轮猜出答案，平均%f轮猜出答案" \
        % (name, array[1], array[2], array[3]))
      player.info[name] = "\t".join([str(x) for x in array])
      response = input("\n是否继续游戏？（输入y继续，其他退出）\n")
      if(response=='y'):
        continue
      else:
        print("退出游戏，欢迎下次再来！\n")
        f=open('game_res.txt', 'w')
        for k in player.info:
          f.write(player.info[k]+'\n')
        f.close()
        break

