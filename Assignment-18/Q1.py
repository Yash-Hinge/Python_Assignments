def Sum(No1=list()):
    Sum =0
    for i in range(len(No1)):
        Sum=Sum + No1[i]


    return Sum


def main():

    Data = list()

    Size = int(input("Enter the number of elements :"))

    for i in range(Size):
        
        no = int(input("enter the number :"))
        Data.append(no)


    ret = Sum(Data)


    print("The Sum of the elements of the list is :",ret)




if __name__ =="__main__":
    main()