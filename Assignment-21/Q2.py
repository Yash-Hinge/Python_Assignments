import threading 
import time

def MaxNum(no):
    ElementMax=no[0]
    print('maximum Element :')
    for i in range(len(no)):
        if(no[i]>ElementMax):
            ElementMax=no[i]
    print(ElementMax)
    




def MinNum(no):
    ElementMin=no[0]
    print("minimum Element : ")
    for i in range(len(no)):
        if(no[i]<ElementMin):
            ElementMin=no[i]
    print(ElementMin)




def main():
    start_time = time.perf_counter()
    
    Num = list()
    Size = int(input("Enter the Size of the list :"))
    for i in range (Size):
        data = int(input("enter the Number :"))
        Num.append(data)
    
    
    Maximum = threading.Thread(target=MaxNum,args=(Num,))

    Minimum = threading.Thread(target=MinNum,args =(Num,))


    

    Maximum.start()
    Maximum.join()
    Minimum.start()
    Minimum.join()
    
    


    end_time =time.perf_counter()

    print(f"Execution Time :{end_time-start_time:.4f}")







if __name__ =="__main__":
    main()


