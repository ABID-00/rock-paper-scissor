import random

array=('r','p','s')

emoji={'r':'🪨','p':'📃','s':'✂️'}

while(1):
    user_input=input('Enter your spell (r,p,s): '.lower())
    if user_input not in array:
        print('Enter valid Input.')
        continue

    comp_inp=array[random.randint(0,2)]
    print('computer choose',emoji[comp_inp])
    print('you choose',emoji[user_input])

    if comp_inp == user_input:
        print('Tie')
    elif(
        (comp_inp=='r'and user_input=='p') 
        or (comp_inp=='p'and user_input=='s')
        or (comp_inp=='s'and user_input=='r')):
        print('you won')
    else:
       print('comp won')
        
    choice= input('Continue(y/n): '.lower())
    if choice=='n':
        break
    
    



    

    
