import random
ran=random.randint(1,10)    
chances=1
while chances<=3:
    guess=int(input('enter the number:'))
    if guess==ran:
        print('congrats')
        break                  #break stops th eexecution
    else:
        chances+=1
        continue                #contunue skip some process or stmts 
if chances>=3:
    print('enter valid input next time')

