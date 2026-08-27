import multiprocessing



def EvenElementCnt(no):

    ElementCnt=0

    for i in range(1,(no+1)):
        if(i%2!=0):
            ElementCnt=ElementCnt+1
    Pid = multiprocessing.current_process().pid
    return ElementCnt, Pid, no 



def main():

    Data = list()

    print("Enter the Number of elements in the list : ")
    Size = int(input())

    for i in range(Size):
        no = int(input("Enter the Data Element:"))
        Data.append(no)

    with multiprocessing.Pool() as pool:

        ret =pool.map(EvenElementCnt,Data)

    for ElementCnt,Pid,no in ret:
        print("Process Id :",Pid)
        print("Input Element :",no)
        print("Output:",ElementCnt)  

        print("\n")      



if __name__ =="__main__" :
    main()