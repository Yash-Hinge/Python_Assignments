import schedule



def DisplayMessage(message):

    print(message)




def main():
    Message = input("Enter The Message to be printed :")

    schedule.every(5).seconds.do(DisplayMessage,Message)  

    while(1):

        schedule.run_pending()




if __name__ =="__main__":
    main()