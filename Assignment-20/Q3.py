import threading 
import time

def EvenListSum(no):
    Even_List_Sum=0
    for i in range(len(no)):
        if(no[i]%2==0):
            Even_List_Sum=Even_List_Sum+no[i]
    print("The Sum of Even List Members  is :",Even_List_Sum)



def OddListSum(no):
    Odd_List_Sum =0
    for i in range(len(no)):
        if(no[i]%2!=0):
            Odd_List_Sum=Odd_List_Sum+no[i]

    print("The Sum of Odd List Members  is :",Odd_List_Sum)





def main():

    start_time = time.perf_counter()
    no = list()
    Size = int(input("enter the number of elements :"))
    
    for i in range (Size):
        din=int(input("Enter The Number :"))
        no.append(din)


    EvenList = threading.Thread(target=EvenListSum,args=(no,))

    OddList = threading.Thread(target=OddListSum,args =(no,))


    EvenList.start()
    
    OddList.start()
   

    end_time =time.perf_counter()

    print(f"Execution Time :{end_time-start_time:.4f}")







if __name__ =="__main__":
    main()


