name="Salad"
price=25.00
q=2

#####################
file=open("persistance/data.txt","w")
file.write(name+","+str(price)+","+str(q))