import random
numberOfStreaks = 0
numofrow = 1
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    list = []
    for i in range(101):
        if random.randint(0,1) == 0:
            list.append('tails')
        else:
            list.append('heads')
    # Code that checks if there is a streak of 6 heads or tails in a row.
    for index3 in range(len(list)):
        try:
            if list[index3] == list[index3+1]:
                numofrow +=1
            else:
                numofrow = 1
                break
            if numofrow >= 6:
                numberOfStreaks +=1
        except IndexError:
            numofrow = 1
            break

print(numberOfStreaks)
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
