from functools import reduce

chkeven = lambda No : (No%2==0)

Square = lambda No : No**2 

Summation  = lambda No1,No2 : No1+No2

def main():
    Data = list()

    Size = int(input("Enter the no. of elements :"))

    for i in range (Size):
        ip = int(input("Enter the Value :"))
        Data .append(ip)


    Fret = list(filter(chkeven,Data))

    print("List after Filter :", Fret )

    Mret = list(map(Square,Fret))
    print("List after Map :",Mret )


    Rret = reduce(Summation,Mret)
    print("list after Reduce :",Rret)



if __name__ =="__main__":
    main()





    