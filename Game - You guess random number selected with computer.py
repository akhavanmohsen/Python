import random
guess = random.randint(1,99)
your_num = int(input('Please enter your guess number : '))
while guess != your_num :
    if guess > your_num :
        print ('Your guess is small ')
    else:
        print ('Your guess is big')
    your_num = int(input('Please enter your guess number : '))
print('WoooooW, You are win')
