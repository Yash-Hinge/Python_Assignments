def prntEven(No):
    Num =1
    i=0
    while(i!=No):
        if(Num%2==0):
            print(Num)
            i=i+1

        Num = Num+1


def main():

    Num = int(input("Enter The Number :"))
    ret = prntEven(Num)
    


if __name__ == "__main__":
    main()