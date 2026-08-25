def Occfreq(No,Ref):
    Freq=0
    for i in range(len(No)):
        if(No[i]==Ref):
            Freq=Freq+1

    return Freq



    


def main():

    Data = list()

    Size = int(input("Enter the number of elements :"))

    for i in range(Size):
        
        no = int(input("enter the number :"))
        Data.append(no)

    element = int(input("Enter the element :"))
    ret = Occfreq(Data,element)


    print("The freq of Occurence of the element in the list is :",ret)




if __name__ =="__main__":
    main()