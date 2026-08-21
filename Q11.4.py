def revNumber(no):
    No=no
    revNum =0
    refno=0

    while(No>0):
        refno=No%10
        revNum=revNum*10+refno
        
        No=No//10
        
        
        
    return int(revNum)


def main():
    no = int(input("enter the number :"))

    ret = revNumber(no)

    print("The revers of  number is :",ret)






if(__name__)=="__main__":
    main()