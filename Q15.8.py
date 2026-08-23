from functools import reduce
prdt = lambda No1,No2 : No1*No2

def main():

    no =list()

    Size = int(input("enter the number of elements :"))

    for i in range(0,Size,1):

        ip=int(input("Enter the number : "))
        no.append(ip)



    
    ret = reduce(prdt, no)

    print("The product is :",ret)


if __name__ =="__main__":
    main()
