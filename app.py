from menu import *
from order import *

option=-1
while option!=0:
    x=loadMenu()
    option=print_menu(x)
    if option==0:
        break
    else:
        process_option(x,option)

    question=input("do you want to see the menu again?")
    if question=="no":
        print("bye")
        break
    else:
        x

    
    

    
    

  
    
   
