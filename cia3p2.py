n=int(input("ENTER THE NUMBER OF ELEMENTS: "))
newlist=[]
for i in range(n):
    newnum=int(input("ENTER THE NUMBER: "))
    newlist.append(newnum)
x=0
for i in newlist:
    if(i==0):
        x+=1
for i in range(x):
    newlist.remove(0)
newlist.sort()
for i in range(x):
    newlist.append(0)
print(newlist)
        
