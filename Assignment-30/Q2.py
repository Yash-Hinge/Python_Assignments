import schedule 
import time 

def printX():
    print(time.ctime())

def main():

    schedule.every(1).minute.do(printX)

    while(1):

        schedule.run_pending()
        time.sleep(30)



if __name__ =="__main__":
    main()