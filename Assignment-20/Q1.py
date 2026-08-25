import threading 
import time

def EvenDisplay(no):
    refNum =0
    NumCnt=1
    while(refNum!=no):
        if(NumCnt%2==0):
            refNum=refNum+1
            print(NumCnt)

        NumCnt=NumCnt+1

def OddDisplay(no):
    refNum =0
    NumCnt=1
    while(refNum!=no):
        if(NumCnt%2!=0):
            refNum=refNum+1
            print(NumCnt)

        NumCnt=NumCnt+1




def main():

    start_time = time.perf_counter()

    Even = threading.Thread(target=EvenDisplay,args=(10,))

    Odd = threading.Thread(target=OddDisplay,args =(10,))


    Even.start()
    Even.join()
    Odd.start()
    Odd.join()

    end_time =time.perf_counter()

    print(f"Execution Time :{end_time-start_time:.4f}")







if __name__ =="__main__":
    main()


