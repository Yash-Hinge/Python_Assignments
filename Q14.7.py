chkDivisible5 = lambda No : bool(No%5==0)



def main():
    Num1 = int(input("Enter the number :"))
   
    ret = chkDivisible5(Num1)


    print("The given Numbers is Divisible by five :",ret)





if __name__=="__main__":
    main()
