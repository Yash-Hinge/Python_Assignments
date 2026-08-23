def chkNum(Num):
    if(Num%2==0):
        print("Even Number ")

    else:
        print("Odd Number")



def main():

    No = int(input("Enter the Number : "))
    chkNum(No)




if __name__ == "__main__":
    main()