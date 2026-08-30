class Numbers :
    

    def __init__(self,Value):
        self.value1=Value
       
                
    def ChkPrime(self):

        for i in range (2,self.value1):
            if(self.value1%i==0):
                return False
            
        return True

    def ChkPerfect(self):
        factSum =0
        for i in range(1,(self.value1+1)):
            if(self.value1%i==0):
                factSum=factSum+i

        if factSum == self.value1:
            return True 
        else:
            return False 

    def factors (self):
        print("Factors : ")
        for i in range (1,(self.value1+1)):
            if(self.value1%i==0):
                print(i)

    def SumFactors(self):
        factSum=0
        for i in range (1,(self.value1+1)):
            if(self.value1%i==0):
                factSum = factSum +i

        return factSum
    


    

def main():

   

    Num = int(input("Enter the number :"))

    Nobj = Numbers(Num)
    ret = Nobj.ChkPrime()
    print("Prime Number : ",ret)

    ret = Nobj.ChkPerfect()
    print("Perfect Number : ",ret)

    ret = Nobj.factors()
    

    ret = Nobj.SumFactors()
    print("Sum of Factors  : ",ret)

   

     

   




if __name__ =="__main__":
    main()