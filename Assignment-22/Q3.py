import multiprocessing
import time


def CntPrimeElements(no):
    factorCnt=0
    PrimeCnt=0
    
    for i in range(1,(no+1)):
        factorCnt=0
        for j in range(1,(i+1)):
                
                if(i%j==0):
                    
                    factorCnt =factorCnt+1
                
        
        if(factorCnt==2):
            PrimeCnt=PrimeCnt+1
    
    return PrimeCnt




def main():
    Start_Time = time.perf_counter()
    Data = list()
    Size = int(input("Enter the number of elements in the list :"))

    for i in range (Size):
        no = int(input("Enter the element : "))
        Data.append(no)


    with multiprocessing.Pool() as pool:

        ret1 =  list(pool.map(CntPrimeElements,Data)) 

    print("The no. of prime elements is :",ret1)


    End_Time =time.perf_counter()

    print(f"Total Execution time : {End_Time-Start_Time:.4f}")


if __name__ =='__main__':
    main()