Product = lambda No1,No2,No3 : max(No1,No2,No3)



def main():
    Num1 = int(input("Enter the number :"))
    Num2 = int(input("Enter the number :"))
    Num3 = int(input("Enter the number :"))
   
    ret = Product(Num1,Num2)


    print("product of Given Numbers is :",ret)





if __name__=="__main__":
    main()
