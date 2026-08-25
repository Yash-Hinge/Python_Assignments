def Maxx(No=list()):
    NumMax =No[0]
    
    for i in range(len(No)):
        if(No[i]>NumMax):
            NumMax=No[i]

    return NumMax



    


def main():

    Data = list()

    Size = int(input("Enter the number of elements :"))

    for i in range(Size):
        
        no = int(input("enter the number :"))
        Data.append(no)


    ret = Maxx(Data)


    print("The Max value  of the elements of the list is :",ret)




if __name__ =="__main__":
    main()