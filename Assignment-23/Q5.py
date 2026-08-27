import multiprocessing



def Factorial(no):

    factorial=1

    for i in range(1,(no+1)):
        factorial = factorial*i
    Pid = multiprocessing.current_process().pid
    return factorial, Pid, no 



def main():

    Data = list()

    print("Enter the Number of elements in the list : ")
    Size = int(input())

    for i in range(Size):
        no = int(input("Enter the Data Element:"))
        Data.append(no)

    with multiprocessing.Pool() as pool:

        ret =pool.map(Factorial,Data)

    for factorial,Pid,no in ret:
        print("Process Id :",Pid)
        print("Input Element :",no)
        print("Output:",factorial)  

        print("\n")      



if __name__ =="__main__" :
    main()