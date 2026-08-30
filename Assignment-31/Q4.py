import schedule
import os
import time 



def CreateLog():
    timestamp =str(time.ctime())
    timestamp =timestamp.replace(" ","_")
    timestamp = timestamp.replace(":","-")
    filename = "Logfile"+timestamp
    fobj = open(filename,"a")
    fobj.write(f"Log create Succesfully\n Created at time :{time.ctime()}")

    print("Log Created Succesfully")




def main():
    

    schedule.every(1).minute.do(CreateLog)  

    while(1):

        schedule.run_pending()




if __name__ =="__main__":
    main()