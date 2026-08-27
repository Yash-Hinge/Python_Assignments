import multiprocessing



def EvenSum(no):

    SumEven=0

    for i in range(1,(no+1)):
        if(i%2==0):
            SumEven=SumEven+i
    Pid = multiprocessing.current_process().pid
    return SumEven, Pid, no 



def main():

    Data = list()

    print("Enter the Number of elements in the list : ")
    Size = int(input())

    for i in range(Size):
        no = int(input("Enter the Data Element:"))
        Data.append(no)

    with multiprocessing.Pool() as pool:

        ret =pool.map(EvenSum,Data)

    for SumEven,Pid,no in ret:
        print("Process Id :",Pid)
        print("Input Element :",no)
        print("Output:",SumEven)  

        print("\n")      



if __name__ =="__main__" :
    main()