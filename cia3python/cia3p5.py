
def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True



print("ENTER THE NUMBER OF ACCOUNT HOLDERS  :",end='')
n=int(input())
accholders=set()
for i in range(n):
    z=int(input("ENTER THE ACCOUNT NUMBER :"))
    accholders.add(z)

print("\nACCOUNT HOLDERS",accholders)
print("\nENTER THE NUMBER OF DEPOSITERS  :",end='')
n=int(input())
i=0
depositers=set()
while(i<n):
     z=int(input("ENTER THE ACCOUNT NUMBER :"))
     if(z in accholders):
         depositers.add(z)
         i+=1
     else:
         print("NUMBER NOT PRESENT TRY AGAIN")
withdrawer=set()
print("\nDEPOSITERS",depositers)
print("\nENTER THE NUMBER OF WITHDRAWERS  :",end='')
n=int(input())
i=0
while(i<n):
     z=int(input("ENTER THE ACCOUNT NUMBER :"))
     if(z in accholders):
         withdrawer.add(z)
         i+=1
     else:
         print("NUMBER NOT PRESENT TRY AGAIN")
print("\nWITHDRAWERS",withdrawer)


l20to50=set()
for i in range(20,50,1):
    if(is_prime(i)):
        l20to50.add(i)
print("\n\nNEW LIST OF ACC HOLDERS",l20to50)
print("WITHDRAWERS IN NEW LIST",l20to50 & withdrawer)
print("DEPOSITERS IN NEW LIST",l20to50 & depositers)
print("THOSE NOT INVOLVED IN DEPOSITERS AND WITHDRAWERS",(l20to50-withdrawer)-depositers)
nl=l20to50.copy()
for i in nl:
    if(i%2==0):
        l20to50.discard(i)

print("FINAL LIST",l20to50)






