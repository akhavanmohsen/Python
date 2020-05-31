import random
mynumer = int(input('Enter your guess number'))
comp_number = random.randint(1,99)
while mynumer != comp_number :
    if mynumer > comp_number :
        print(comp_number, '< my guess number, select bigger ')
        comp_number = random.randint(comp_number,mynumer)
    else:
        print(comp_number, '> my guess number, select smaller')
        comp_number = random.randint(mynumer,comp_number)
print('Excellent, You guess', comp_number , 'So you are win')
