file = open("persistance/data.txt","r")
data=file.read()

print(data)
print(type(data))


# #parse data |Method1:
# name  = data[:6]
# price = float(data[6:12])
# q     = int(data[-1:])
# total=q*price
# print(name,price,q,"=",total)

#parse data |Method2:

segments = data.split(",")
name=segments[0]
price=float(segments[1])
q= int(segments[2])
total=q*price
print(segments) 
print(name)
print(price)
print(q)
print(total)