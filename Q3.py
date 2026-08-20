def factorial(no1):
    fact=1
    for i in range(1,(no1+1)):
        fact= fact*i

    return fact






def main():
    no=int(input("enter the number:"))

    ret = factorial(no)
    print("The factorial is :",ret)





if(__name__)=="__main__":
    main()