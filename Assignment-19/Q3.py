from functools import reduce

chkRange = lambda No :(No>=70 and No<=90)

increament = lambda No : No+10 

Multiplication = lambda No1,No2 : No1*No2

def main():
    Data = list()

    Size = int(input("Enter the no. of elements :"))

    for i in range (Size):
        ip = int(input("Enter the Value :"))
        Data .append(ip)


    Fret = list(filter(chkRange,Data))

    print("List after Filter :", Fret )

    Mret = list(map(increament,Fret))
    print("List after Map :",Mret )


    Rret = reduce(Multiplication,Mret)
    print("list after Reduce :",Rret)



if __name__ =="__main__":
    main()





    