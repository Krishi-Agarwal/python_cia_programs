print("Program to read a string and extract the details")
string=input("Please enter the string for which the details you need of: ")
numbers=0
alphabets=0
cap=0
low=0
words=0
space=0
string=string.strip()
for i in string:
    if(i.isdigit()==True):
        numbers+=1
    if(i.isalpha()==True):
        alphabets+=1
    if(i.isupper()==True):
        cap+=1
    if(i.islower()==True):
        low+=1
    if(i==' '):
        space+=1
words=len(string.split())
print("Number of Words :",words)
print("Number of Spaces :",space)
print("Number of digits :",numbers)
print("Number of alphabets :",alphabets)
print("Number of lower case alphabets :",low)
print("Numebr of upper case alphabets :",cap)