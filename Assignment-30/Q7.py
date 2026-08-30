import schedule 
import time 
import shutil

def BackupFile(Srcfilepath,Backfilepath):
    
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
   
    backfilename = f"{Backfilepath}_{timestamp}"
    

    

    shutil.copy(Srcfilepath,backfilename)
    
    logfobj=open("Backup_Log","a")
    logfobj.write(f"Backup Succesfully Completed at time :{timestamp}\n")

    print("Succesfully Backup!!")

def main():
    Srcfilepath=input("Enter the SrcFile path :")
    Backfilepath=input ("Enter the Destination file path : ")
    



    schedule.every(1).hour.do(BackupFile,Srcfilepath,Backfilepath)

    while(1):

        schedule.run_pending()
        time.sleep(30)



if __name__ =="__main__":
    main()