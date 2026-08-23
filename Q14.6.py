chkOdd = lambda No : bool(No%2!=0)



def main():
    Num1 = int(input("Enter the number :"))
   
    ret = chkOdd(Num1)


    print("The given Numbers is Odd :",ret)





if __name__=="__main__":
    main()
