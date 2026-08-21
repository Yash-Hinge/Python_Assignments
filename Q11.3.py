def SumDigits(no):
    No=no
    Sum =0
    refno=0

    while(int(No)!=0):
        refno=No%10
        Sum=Sum+refno
        No=No/10
        
    return int(Sum)


def main():
    no = int(input("enter the number :"))

    ret = SumDigits(no)

    print("The Sum of Digits in the number is :",ret)






if(__name__)=="__main__":
    main()