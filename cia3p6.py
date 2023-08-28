from xml.sax.xmlreader import IncrementalParser


def details():
    fees=int(input("ENTER THE FEES PER HOUR :"))
    otfees=int(input("ENTER THE FEES FOR OVER TIME :"))
    hr=int(input("ENTER THE NUMBER OF HOURS WORKED :"))
    
    othr=int(input("OVER TIME HOUR DETAILS :"))
    salary=(hr-othr)*fees+othr*otfees
    return salary

def furthersums(bs):
    TOTALSALARY=details()+bs

    return TOTALSALARY

def display(**dic):
    for key,pair in dic.items():
        print(f"{key}={pair}")


def acceptemployees(n):
    listofpayments=dict()
    total=0

    for i in range (n):
        print(f"\n\nENTER THE NAME OF EMPLOYEE {i+1} :",end="")
        name=input()
        basesalary=int(input("ENTER THE BASE SALARY :"))
        TOTALSALARY=0
        pay=(furthersums(bs=basesalary))
        print(f"SALARY FOR THE {name} IS {pay}")
        total+=pay
        listofpayments[name]=pay

    print(f"TOTAL SALARY TO ALL THE EMPLOYEES {total}")
    print("\n\nFINAL LIST OF NAMES ALONG WITH SALARY")
    display(**listofpayments)


def main():
    print("WELCOME TO PAYROLL")
    n=int(input("ENTER THE NUMBER OF EMPLOYEES WHOSE PAYROLL HAS TO BE CALCULATED :"))
    acceptemployees(n)
main()
