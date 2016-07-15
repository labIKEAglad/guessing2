import random
num=random.randint(1,10)

while 1:
    a=raw_input('Please input number between 1~10:')

    if int(a)==num:
        print 'BINGO,YOURE RIGHT!'
        break
    else:
        print 'Please Try Again!'
    
