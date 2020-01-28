print('How many cats do you have?')
numCats = input()
try:
    if int(numCats) >= 4:
        print('That is a lot of cats.')
    elif int(numCats) > -1:
        print('That is not that many cats.')
    else:
        print('You can\'t have negative cats silly')
except ValueError:
    print('You did not enter a number.')
