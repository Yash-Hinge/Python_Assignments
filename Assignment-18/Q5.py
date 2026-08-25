from MarvellousNumX import chkPrime
def ListPrime(No):
    SumPrime=0
    for i in range(len(No)):
        ret = chkPrime(No[i])
        if ret is True:
            SumPrime=SumPrime+No[i]

    return SumPrime
    



    


def main():

    Data = list()

    Size = int(input("Enter the number of elements :"))

    for i in range(Size):
        
        no = int(input("enter the number :"))
        Data.append(no)

    
    ret = ListPrime(Data)


    print("The sum of Prime  element in the list is :",ret)




if __name__ =="__main__":
    main()