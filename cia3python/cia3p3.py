from pickle import APPEND


n=int(input("ENTER THE NUMBER OF PRODUCTS:"))
total=()

i=0
max1=0
name1=''
while(i < n):
    i+=1
    a=input("\nEnter the product name : ")
    b=int(input("ENTER THE QUANTITY : "))
    c=int(input("ENTER THE PRICE : "))
    d=b*c
    if(d>max1):
        max1=d
        name1=a
    tuple1=(a,b,c,d)
    print(tuple1)
    total=total+(tuple1,)
    
print("\n\nFINAL TUPLE : ",total)
sum=0
for i in total:
    sum+=i[3]
print("\n\ntotal sales",sum)
print(f"\n\nELEMENT WITH MAX REVENUE IS '{name1}' revenue being '{max1}'")


    



