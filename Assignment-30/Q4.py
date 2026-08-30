import schedule 
import time 

def printX():
    print("Namaskar")

def main():

    schedule.every().day.at("9:00").do(printX)

    while(1):

        schedule.run_pending()
        time.sleep(750)



if __name__ =="__main__":
    main()