import threading 
import time

def EvenFactorSum(no):
    Even_fact_Sum=0
    for i in range(1,(no+1)):
        if(no%i==0):
            if(i%2==0):
                Even_fact_Sum=Even_fact_Sum+i
    print("The Sum of Even factors is :",Even_fact_Sum)



def OddFactorSum(no):
    Odd_fact_Sum =0
    for i in range(1,(no+1)):
        if(no%i==0):
            if(i%2!=0):
                Odd_fact_Sum=Odd_fact_Sum+i

    print("The Sum of Odd factors is :",Odd_fact_Sum)





def main():

    start_time = time.perf_counter()
    no = int(input("Enter The Number :"))

    EvenFactor = threading.Thread(target=EvenFactorSum,args=(no,))

    OddFactor = threading.Thread(target=OddFactorSum,args =(no,))


    EvenFactor.start()
    
    OddFactor.start()
    

    print("Exit from main..")
    end_time =time.perf_counter()

    print(f"Execution Time :{end_time-start_time:.4f}")







if __name__ =="__main__":
    main()


