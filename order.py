
# module: order functionality

def process_option(food,option):
    
    
    food_name=list(food.keys())[option-1]
    food_price=food[food_name]
    

    print(food_name)

    quantity=input("how many?")

    my_order={}



    if quantity=="":
        print("You have canceled the order")
        
    elif int(quantity)>=0:
        cost=int(quantity)*food_price
        print("You have chosen",int(quantity),food_name,"x",food_price,"|=>",int(quantity)*food_price )
        my_order={food_name:quantity}
        print(my_order)


    answer=str(input("Would you like anything else?"))

    if answer=="yes":
        return food_name
    elif answer=="no":
        client_name=input("Your name please: ")
        file = open("persistance/restaurant_app/data/"+ client_name+"-order.txt","w")
        file.write(food_name+"|"+str(quantity)+"|"+str(food_price)+"|"+str(cost))
    print("Have a nice day "+client_name)
    
                



    
    


   