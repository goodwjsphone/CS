outlets=[]
outlet1=[10,12,15,10]
outlet2=[5,8,3,6]
outlet3=[10,12,15,10]
outlets.append(outlet1)
outlets.append(outlet2)
outlets.append(outlet3)

total = 0

for x in range(3):
    for y in range(4):
        total += outlets[x][y]
    print ("total of outlet " +str(x+1) + " was " + str(total))
    total = 0 
