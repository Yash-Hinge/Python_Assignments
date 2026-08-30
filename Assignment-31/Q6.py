import schedule
import os
import time 

def Monday():
    print("Start Your Weekly Goal.")


def Wednesday():
    print("Review Your Weekly Progress.")

def friday():
    print("Weekly Work Completed")

def main():
    

    schedule.every().monday.at("9:00").do(Monday)
    schedule.every().wednesday.at("17:00").do(Wednesday)
    schedule.every().friday.at("18:00").do(friday)


    while(1):

        schedule.run_pending()
        time.sleep(45)



if __name__ =="__main__":
    main()