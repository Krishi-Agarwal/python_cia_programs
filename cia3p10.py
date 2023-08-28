sum=0

def addnumbers(a,b):
    try:
        
        
        sum=a+b
    except TypeError:
        print("both the number should be of same data type")       
    else:
        print("sum is",sum)
    finally:
        print("PROGRAM CREATED BY KRISHI HAS BEEN EXECUTED SUCCESFULLY")
addnumbers(5,10)
addnumbers(5,"krishi")
