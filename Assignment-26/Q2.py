


class Circle:
    PI=3.14

    def __init__(self):
        self.radius=0
        self.area =0
        self.circumference=0

    def accept(self):
        self.radius = float(input("Enter the Radius :"))
        
        
    def calculatearea(self):
        self.area = Circle.PI * (self.radius**2)

    def calculateCircumference(self):
        self.circumference= 2*Circle.PI*self.radius

    def Display(self):
        print("radius :",self.radius)
        print("area :",self.area)
        print("circumference :",self.circumference)
        print("\n")


def main():



    Cobj1 = Circle()

    Cobj1.accept()
    Cobj1.calculatearea()
    Cobj1.calculateCircumference()
    Cobj1.Display()

    Cobj2 = Circle()

    Cobj2.accept()
    Cobj2.calculatearea()
    Cobj2.calculateCircumference()
    Cobj2.Display()
    






if __name__ =="__main__":
    main()