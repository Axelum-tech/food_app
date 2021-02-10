#Module: menu functionalities
def loadMenu():
    file=open("persistance/restaurant_app/data/food.txt","r")
    data=file.read()

    lines=data.split()
    food={}
    for line in lines:
        segs=line.split("|")
        food[segs[0]]=float(segs[1])
    return food

def print_menu(food):
    from os import system
    print("########### MENU ###########")
    print("0 EXIT")
    n=1
    for f in food :
        print(n,f)
        n+=1
    
    print("########### MENU ###########")
    
    option= int(input("Choose>>>>>"))
    system("cls")
    return option

    

        

