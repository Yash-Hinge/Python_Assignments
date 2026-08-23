def chkPerfect(num):
    factSum =0

    for i in range(1,num):
        if(num%i ==0):
            factSum = factSum+i

    
    if(factSum==num):
        return True
    
    else:
        return False





def main():
    Num = int(input("enter the Number:"))
   

    ret = chkPerfect(Num)

    if(ret == True ):
        print("The number is perfect .")

    else :
        print("the number is not perfect.")




if(__name__)=="__main__":
    main()