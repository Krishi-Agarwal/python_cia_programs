class krishi():
    def __init__(self,a,b):
        print("THIS PROGRAM IS CREATED JUST TO REFER TO THE CONCEPTS DISCUSSED IN CLASS")

        print("\nEXECUTING CONSTRUCTOR")
        print("\nPrint the string parameter isnide constructor",a)
        print("Printing the list parameter inside the constructor",b)
        self.a1=a
        b.append("THE LIST WASS PASSED")
        self.b1=b
    def __del__(self):
        print("\n\nTHE OBJECT HAS BEEN DELETED")
    def funct(self):
        print("\n\nEXECUTING FUNCTION")
        print("\n\nPRINTING THE VARIABLE REFERING THE CONSTRUCTOR")
        print(self.a1)
        print(self.b1)
    
obj = krishi("NORMAL STRING",["SENDING A LIST WITH A STRING"])
obj.funct()
del obj





