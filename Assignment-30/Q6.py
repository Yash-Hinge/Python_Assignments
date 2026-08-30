import schedule 
import time 

def LunchTime():
    print("Lunch Time !")


def PackUp():
    print("Wrap UP Work")
def main():

    schedule.every().day.at("13:00").do(LunchTime)
    schedule.every().day.at("18:00").do(PackUp)

    while(1):

        schedule.run_pending()
        time.sleep(240)



if __name__ =="__main__":
    main()