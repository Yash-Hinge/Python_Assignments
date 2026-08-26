import threading 
import time 


lock =threading.Lock()
Counter =0
def incSharedCounter(No):
    global Counter 
    instanceCounter=0
    for i in range (No):
        with lock :
            instanceCounter = Counter 
            print("The thread name is ",threading.current_thread().name)
            Counter =instanceCounter+1
             

    


def main():

    Num = int(input("Enter the Number of iterations :"))
     

    t1 = threading.Thread(target=incSharedCounter,args=(Num,))
    t2 = threading.Thread(target=incSharedCounter,args=(Num,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("The value of Counter is :",Counter)  







if __name__ =="__main__":
    main()
