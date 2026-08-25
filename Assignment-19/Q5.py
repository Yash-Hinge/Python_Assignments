from functools import reduce

def chkPrime(No):
    for i in range(2,No):
        if(No%i==0):
            return False 
        
    return True 

Multiply = lambda No : No*2 

def findMax(No1,No2):
    elementmax = No1
    if(No2>elementmax):
        elementmax=No2
    

    return elementmax


def main():
    Data = list()

    Size = int(input("Enter the no. of elements :"))

    for i in range (Size):
        ip = int(input("Enter the Value :"))
        Data .append(ip)


    Fret = list(filter(chkPrime,Data))

    print("List after Filter :", Fret )

    Mret = list(map(Multiply,Fret))
    print("List after Map :",Mret )


    Rret = reduce(findMax,Mret)
    print("list after Reduce :",Rret)



if __name__ =="__main__":
    main()





    