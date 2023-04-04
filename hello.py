import random
num = 0


while num <= 5 :
    dice = random.randint(1,6)
    if dice %2 == 0 :
        num += 1
    print('Dice roll : ', dice)
    if num == 5 :
        break
print('End of rolling dice')