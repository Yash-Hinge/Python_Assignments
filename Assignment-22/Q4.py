import multiprocessing
import time 


def CalculatePower(no):
    result =0
    for i in range (1,(no+1)):
        result = result+(i**5)



    return result



def main():

    Data = list()
    Size = int(input("Enter the size of list :"))

    for i in range(Size):
        no = int(input("Enter the element :"))
        Data.append(no)


    
    with multiprocessing.Pool() as pool:

        ret = list(pool.map(CalculatePower,Data))

        print("The result is ",ret )

    

if __name__ =="__main__":
    main()
