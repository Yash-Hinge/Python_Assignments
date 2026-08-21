def Arithematics(num1,num2):
    return num1+num2,num1-num2,num1*num2,num1/num2

    






def main():
    No1=int(input("Enter the 1st Number :"))
    No2=int(input("Enter the 2nd  Number :"))

    ret1,ret2,ret3,ret4=Arithematics(No1,No2)

    print("the sum is :",ret1)
    print("the difference is :",ret2)
    print("the product is :",ret3)
    print("the division is :",ret4)
  




if(__name__)=="__main__":
    main()