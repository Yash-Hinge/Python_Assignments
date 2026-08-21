def chckPalidrome(no):
    No=no
    revNum =0
    refno=0

    while(No>0):
        refno=No%10
        revNum=revNum*10+refno
        
        No=No//10
        
        
        
    if(no==revNum):
        return True
    
    else:
        return False 


def main():
    no = int(input("enter the number :"))

    ret = chckPalidrome(no)

    if ret is True:
        print("the  number is palindrome .")


    else :
        print("the number is not palidrome ")






if(__name__)=="__main__":
    main()