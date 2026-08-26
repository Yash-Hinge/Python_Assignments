import threading 
import time 


lock =threading.Lock()
Addition =0
Prdt =0
def SumList(No,result):
    global Addition 
    
    for i in range (len(No)):
        Addition = Addition+No[i]
    

def PrdtList(No,result):
    global Prdt
    Prdt=1
    for i in range(len(No)):
        Prdt=Prdt*No[i]
    
    

def main():

    Data = list()
    print ("Enter the no. of elements in the list :")
    Size = int(input())
    result=0
    print("Enter the Elements :")

    for i in range(Size):
        no = int(input())
        Data.append(no)


    Sum = threading.Thread(target=SumList,args =(Data,result))
    Product = threading.Thread(target=PrdtList,args =(Data,result))

    Sum.start()
    Product.start()

    Sum.join()
    Product.join()

    print("The Sum of the elements is :",Addition)
    print("The Product is : ",Prdt)

if __name__ =="__main__":
    main()
