def cntDigits(no):
    No=no
    Cnt =0
    while(int(No)!=0):
        
        No=No/10        
        Cnt=Cnt+1
    
    return Cnt


def main():
    no = int(input("enter the number :"))

    ret = cntDigits(no)

    print("The number of Digits in the number is :",ret)






if(__name__)=="__main__":
    main()