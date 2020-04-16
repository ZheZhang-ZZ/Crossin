from random import randint

answer = randint(1,100)
#answer=50
print('''Welcome to guess_number game.
You can stop the game by inputing a negative number.''')

finish=0
numOfRound=0
totRound=1
totGuess=0

while True:
  guess = int(input('Guess...\n'))
  totGuess+=1
  if(guess<0):
    finish=-1
    break
  elif(guess<1 or guess >100):
    print('''Warning: Out of range!!!
Your guess must be within [1,100]''')
    continue
  else:
    numOfRound+=1
    if(guess>answer):
      print("Too Big")
    elif(guess<answer):
      print("Too small")
    else:
      print("Bingo")
      print("You have guessed %d times to get the right answer" % numOfRound)
      response = input("\nDo you want to continue? Y or N\n")
      if(response=='Y'):
        answer = randint(1,100)
        numOfRound=0
        totRound+=1
        continue
      else:
        finish=1
        break

if(finish==1):
  print("You have played %d rounds, \
and in average you guessed %.2f times to get it" % (totRound, float(totGuess)/totRound))
elif(finish==-1):
  print("Oops, Stopped! Bye!\n")
