chkEven = lambda No : bool(No%2==0)



def main():
    Num1 = int(input("Enter the number :"))
   
    ret = chkEven(Num1)


    print("The given Numbers is even :",ret)





if __name__=="__main__":
    main()
