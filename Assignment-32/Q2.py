import schedule 
import time 
import os



def MonitorfileSize(Filepath):
    

    if(os.path.exists(Filepath)):
        fobj =open("FileLogSize.txt" ,"a")
        fobj.write(f"{Filepath}\n")
        fobj.write(f"{os.path.getsize(Filepath)}\n")
        fobj.write(f"{time.ctime()}\n")
    print("File Created Succesfully...")





def main():
    Filepath = input("enter the filename or path :")

    schedule.every(30).seconds.do(MonitorfileSize,Filepath)


    while(1):
        schedule.run_pending()
        time.sleep(45)




if __name__=="__main__":
    main()