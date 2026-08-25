import threading 
import time

def FindSmall(no):
    small_char_cnt=0
    for i in range(len(no)):
        if(no[i]>='a' and no[i]<='z'):
           small_char_cnt = small_char_cnt+1

    print("The thread id Is :",threading.get_ident())
    print("The name of thread is ",threading.current_thread().name)
    print("The Count of Small case List Members  is :",small_char_cnt)



def FindCapital(no):
    Capital_char_cnt=0
    for i in range(len(no)):
        if(no[i]>='A' and no[i]<='Z'):
           Capital_char_cnt = Capital_char_cnt+1

    print("The thread id Is :",threading.get_ident())
    print("The name of thread is ",threading.current_thread().name)
    print("The Count of Capital case List Members  is :",Capital_char_cnt)

def FindNum(no):
    Num_cnt=0
    for i in range(len(no)):
        if(no[i]>='0' and no[i]<='9'):
           Num_cnt = Num_cnt+1
    
    print("The thread id Is :",threading.get_ident())
    print("The name of thread is ",threading.current_thread().name)
    print("The Count of Numeric List Members  is :",Num_cnt)



def main():
    start_time = time.perf_counter()
    
    Str =  input("Enter the String : ")
    
    
    Small = threading.Thread(target=FindSmall,args=(Str,))

    Capital = threading.Thread(target=FindCapital,args =(Str,))

    Number = threading.Thread(target = FindNum,args=(Str,))


    Small.start()
    
    Capital.start()
    
    Number.start()
    

    end_time =time.perf_counter()

    print(f"Execution Time :{end_time-start_time:.4f}")







if __name__ =="__main__":
    main()


