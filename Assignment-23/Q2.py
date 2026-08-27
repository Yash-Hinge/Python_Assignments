import multiprocessing



def OddSum(no):

    SumOdd=0

    for i in range(1,(no+1)):
        if(i%2!=0):
            SumOdd=SumOdd+i
    Pid = multiprocessing.current_process().pid
    return SumOdd, Pid, no 



def main():

    Data = list()

    print("Enter the Number of elements in the list : ")
    Size = int(input())

    for i in range(Size):
        no = int(input("Enter the Data Element:"))
        Data.append(no)

    with multiprocessing.Pool() as pool:

        ret =pool.map(OddSum,Data)

    for SumOdd,Pid,no in ret:
        print("Process Id :",Pid)
        print("Input Element :",no)
        print("Output:",SumOdd)  

        print("\n")      



if __name__ =="__main__" :
    main()