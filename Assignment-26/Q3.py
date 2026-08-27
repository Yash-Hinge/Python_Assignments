


class Arithematics:
    PI=3.14

    def __init__(self):
        self.Value1=0
        self.Value2 =0
        

    def accept(self):
        self.Value1 = float(input("Enter the No1 :"))
        self.Value2 = float(input("Enter the No2 : "))
        
        
    def Addition(self):
        self.Sum = self.Value1+self.Value2

    def Subtarction(self):
        self.Difference = self.Value1-self.Value2

    def Multiplication(self):
        self.Product = self.Value1 * self.Value2

    def Division(self):
        self.division = self.Value1/self.Value2

    def Display(self):
        print("Sum :",self.Sum)
        print("Difference :",self.Difference)
        print("Multiplication :",self.Product)
        print("Division : ",self.division)
        print("\n")


def main():

    Aobj1= Arithematics()
    Aobj1.accept()
    Aobj1.Addition()
    Aobj1.Subtarction()
    Aobj1.Multiplication()
    Aobj1.Division()
    Aobj1.Display()

    Aobj2= Arithematics()
    Aobj2.accept()
    Aobj2.Addition()
    Aobj2.Subtarction()
    Aobj2.Multiplication()
    Aobj2.Division()
    Aobj2.Display()
    
    







if __name__ =="__main__":
    main()