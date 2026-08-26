import multiprocessing
import time 



def CalculateFactorial(no):
    Factorial=1
    for i in range(1,no+1):
        Factorial =Factorial*i

    multiprocessing.current_process().pid
    return Factorial,multiprocessing.current_process().pid,no




def main():
    with multiprocessing.Pool() as pool:
        start_time = time.perf_counter()
        Data = list()
        Size=int(input("Enter the no.of elemnets :"))
        for i in range (Size):
            no = int(input("Enter the element : "))
            Data.append(no)



        ret1,ret2,ret3 = list(pool.map(CalculateFactorial,Data))

        print("Factorials are  :",ret1,"\n")
        print("Process Id:",ret2,"\n")
        print("input Values :",ret3)

        end_time =time.perf_counter()


        print(f"Total time :{end_time-start_time:.4f}")




if __name__ =="__main__":
    main()