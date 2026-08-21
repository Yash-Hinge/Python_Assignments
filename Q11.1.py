def checkPrime(no):
    for i in range(2,no):
        if(no%i==0):
            return False
               
        else :
            return True



def main():
    no = int(input("enter the umber :"))

    ret = checkPrime(no)

    if(ret==True):
        print("The entered number is prime .")

    else :
        print("the entered number is composite .")






if(__name__)=="__main__":
    main()