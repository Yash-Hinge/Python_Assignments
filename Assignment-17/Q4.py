def factorSum(no):
    factSum =0
    for i in range(1,((no//2)+1)):
        if (no%i==0):
            factSum = factSum + i

    return factSum
        

    





def main():

    no = int(input("enter the number :"))

    ret = factorSum(no)

    print("The sum of factors  is : ",ret )




if __name__ =="__main__":
    main()

