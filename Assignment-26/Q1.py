


class Demo:
    Value1 =100

    def __init__(self,a,b):
        self.No1=a
        self.No2 =b

    def fun(self):
        print("Values :",self.No1,",",self.No2)
        
    def gun(self):
        print("Values : ",self.No1,",",self.No2)



def main():

    Num1=int(input("Enter the first element :"))

    Num2 = int(input("Enter the second element :"))


    dobj = Demo(Num1,Num2)

    dobj.fun()
    dobj.gun()






if __name__ =="__main__":
    main()