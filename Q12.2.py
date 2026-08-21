def Factors(num):
    for i in range(1,(num+1)):
        if(num%i==0):
            print(i)
    






def main():
    No=int(input("Enter the Number:"))
    Factors(No)




if(__name__)=="__main__":
    main()