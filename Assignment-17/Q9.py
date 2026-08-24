def Numlen(No1):
    Len=0
    while(No1!=0):
        Len = Len+1
        No1=No1//10

    return Len



def main():

    no = int(input("enter the number :"))

    ret = Numlen(no)
    print("The length of Number is :",ret)




if __name__ =="__main__":
    main()