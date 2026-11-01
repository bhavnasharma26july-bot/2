num=35
i=1
heart=5 
while i<=5:
   
     answer=int(input('enter your guess for the number'))
     if answer==35:
      print('congrats you have guessed correctly')
     elif not answer==35:
       print('hard luck try again,lives left',heart-1)
     else:
       print('kindly add an value between 1 to 50') 
while heart<=0:
    heart=heart-1

    i=i+1  
    
    