Even= lambda no : (no%2==0)

def main():

    no =list()

    Size = int(input("enter the number of elements :"))

    for i in range(0,Size,1):

        ip=int(input("Enter the number : "))
        no.append(ip)



    
    ret = list(filter(Even,no))

    print(ret)


if __name__ =="__main__":
    main()
