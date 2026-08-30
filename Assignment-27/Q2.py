class BankAccount :
    ROI =10.5

    def __init__(self,Name,Amount):
        self.AccHoldername=Name
        self.AccBalance=Amount
                



    def Display(self):

        print("AccHolder Name : ",self.AccHoldername,"\n","Current Balance : ",self.AccBalance)
        print("\n")

    def Deposit(self,DepAmount):
        
        self.AccBalance = self.AccBalance+DepAmount

    def withdrawal(self,WithdrawAmt):
        if(WithdrawAmt<=self.AccBalance):
            self.AccBalance = self.AccBalance-WithdrawAmt
        else:
            print("Insufficient Balance ..")


    def CalculateIntrest(self):
        self.Intrest = (self.AccBalance*BankAccount.ROI)/100
        return self.Intrest


    


    

def main():

    name  = input("Enter the AccHolder Name  :")

    initialAmt = int(input("Enter the initial Amount :"))


    Bobj1 = BankAccount(name,initialAmt) 

    Bobj1.Display()
    DepositAmt =int(input("Enter the Deposit Amount:"))
    Bobj1.Deposit(DepositAmt)
    Bobj1.Display()

    WithdrawAmt =int(input("Enter the Withdrawal Amount:"))
    Bobj1.withdrawal(WithdrawAmt)
    Bobj1.Display()

    ret =Bobj1.CalculateIntrest()

    print("Intrest :",ret)
    

     

   




if __name__ =="__main__":
    main()