import threading 
import time

def printNum(no):
    print("Number in forward Sequence :")
    for i in range(1,(no+1)):
        print(i)




def printNumRev(no):
    print("Number in reverse Sequence :")
    for i in range(no,0,-1):
        print(i,"\t")





def main():
    start_time = time.perf_counter()
    
    Num =  int(input("Enter the Number : "))
    
    
    Thread1 = threading.Thread(target=printNum,args=(Num,))

    Thread2 = threading.Thread(target=printNumRev,args =(Num,))




    Thread1.start()
    Thread1.join()
    Thread2.start()
    Thread2.join()
    
    

    end_time =time.perf_counter()

    print(f"Execution Time :{end_time-start_time:.4f}")







if __name__ =="__main__":
    main()


