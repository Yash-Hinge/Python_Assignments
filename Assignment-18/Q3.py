def Minn(No=list()):
    NumMin =No[0]
    
    for i in range(len(No)):
        if(No[i]<NumMin):
            NumMin=No[i]

    return NumMin



    


def main():

    Data = list()

    Size = int(input("Enter the number of elements :"))

    for i in range(Size):
        
        no = int(input("enter the number :"))
        Data.append(no)


    ret = Minn(Data)


    print("The Min value  of the elements of the list is :",ret)




if __name__ =="__main__":
    main()