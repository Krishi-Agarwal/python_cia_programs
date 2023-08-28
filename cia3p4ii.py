a=input("ENTER THE ITEMS SEPERATED WITH A SINGLE SPACE:")
list1=list(a.split())
print(list1)
dict1={}
for i in list1:
    if(i in (dict1.keys())):
        dict1[i]+=1
    else:
        dict1.update({i:1})
print(dict1)
