name = input('Enter your name    ')

if len(name) <= 1:
    print("Sorry, username must be longer than one letter.")

elif len(name) > 20:
    print("Sorry, username cannot be more than 20 letters in length.")
else:
    for a in name:
         if (a.isdigit()):
            isNumber = True
            
         if(x.isupper()):
            isUpper = True  
       

if(isUpper == False and isNumber == False):
   print( "Sorry, Please re enter name.") 
else:
    print("done!")
