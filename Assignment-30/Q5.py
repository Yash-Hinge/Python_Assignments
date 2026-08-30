import schedule 
import time 

def WriteFile():
    fobj = open("Marvellous.txt","a")
    fobj.write(time.ctime()+"\n")

    print("Succesfully Written!!")

def main():

    schedule.every(5).minutes.do(WriteFile)

    while(1):

        schedule.run_pending()
        time.sleep(60)



if __name__ =="__main__":
    main()