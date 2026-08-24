def checkPrime(no):
    factSum =0
    for i in range(2,no):
        if (no%i==0):
            return False
        
    return True

    
        

    





def main():

    no = int(input("enter the number :"))

    ret = checkPrime(no)

    if(ret==True):
        print("It is prime .")

    else:
        print("It is not prime .")




if __name__ =="__main__":
    main()

