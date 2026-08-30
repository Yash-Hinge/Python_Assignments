import schedule 
import time 

def printX():
    print("Jay Ganesh.... ")

def main():

    schedule.every(2).seconds.do(printX)

    while(1):

        schedule.run_pending()
        time.sleep(1)



if __name__ =="__main__":
    main()