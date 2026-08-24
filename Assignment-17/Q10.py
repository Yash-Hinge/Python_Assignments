def NumDigitSum(No1):
    SumDigit=0
    while(No1!=0):
        SumDigit = SumDigit + No1%10
        No1=No1//10


    return SumDigit



def main():

    no = int(input("enter the number :"))

    ret = NumDigitSum(no)
    print("The Sum of Digit of Number  is :",ret)




if __name__ =="__main__":
    main()