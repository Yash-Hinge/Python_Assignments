import threading 
import time

def PrimeNum(no):
    print("prime Elements:")
    for i in range(1,len(no)):
        if(no[i]%i!=0):
            print(no[i])




def NonPrimeNum(no):
    print("non-prime Elements:")
    for i in range(1,len(no)):
        if(no[i]%i==0):
            print(no[i])





def main():
    start_time = time.perf_counter()
    
    Num = list()
    Size = int(input("Enter the Size of the list :"))
    for i in range (Size):
        data = int(input("enter the Number :"))
        Num.append(data)
    
    
    Prime = threading.Thread(target=PrimeNum,args=(Num,))

    NonPrime = threading.Thread(target=NonPrimeNum,args =(Num,))




    Prime.start()
    Prime.join()
    NonPrime.start()
    NonPrime.join()
    
    

    end_time =time.perf_counter()

    print(f"Execution Time :{end_time-start_time:.4f}")







if __name__ =="__main__":
    main()


