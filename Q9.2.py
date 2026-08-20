def ChkGreater(No1,No2):
    if(No1>No2):
        return No1

    elif(No2>No1):
        return No2

    else:
        return 0




def main():
    print("Enter the first Number")
    Num1=int(input())
    print("Enter the Second Number")
    Num2=int(input())


    ret = ChkGreater(Num1,Num2)

    if(ret==0):
        print("both numbers are same or equal .")

    else:

        print("print the greater number is :",ret)




if(__name__)=="__main__":
    main()