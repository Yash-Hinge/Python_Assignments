import schedule



def PrintX(message):

    print(message)




def main():
    Message = input("Enter The Message to be printed :")
    Time_Interval= int(input("Enter the time Interval in Minutes  :"))

    schedule.every(Time_Interval).minutes.do(PrintX,Message)  

    while(1):

        schedule.run_pending()




if __name__ =="__main__":
    main()