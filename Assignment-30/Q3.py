import schedule 
import time 

def printX():
    print("Coding Kar...!")

def main():

    schedule.every(30).minutes.do(printX)

    while(1):

        schedule.run_pending()
        time.sleep(750)



if __name__ =="__main__":
    main()