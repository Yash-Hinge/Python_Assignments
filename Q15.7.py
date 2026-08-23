
Len = lambda Data : (len(Data)>5)

def main():

    no =list()

    Size = int(input("enter the number of elements :"))

    for i in range(0,Size,1):

        ip=input("Enter the number : ")
        no.append(ip)



    
    ret= list(filter(Len, no))

    print(ret)


if __name__ =="__main__":
    main()
