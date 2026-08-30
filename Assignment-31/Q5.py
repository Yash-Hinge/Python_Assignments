import schedule
import os
import time 

def DirectoryScan(Directory):
    if(os.path.isdir(Directory)):
        timestamp =str(time.ctime())
        timestamp =timestamp.replace(" ","_")
        timestamp = timestamp.replace(":","-")
        filename = "DirectoryLogfile"+timestamp
        fobj = open(filename,"a")
        Filenum=0
        SubDirectoryCnt =0
        for Folders,subfolders,files in os.walk(Directory):
            Filenum=Filenum +len(files)
            SubDirectoryCnt=SubDirectoryCnt+len(subfolders)

        fobj .write(f"Directory Name :{Directory}\n")
        fobj .write(f"Total Files  :{Filenum}\n")
        fobj .write(f"Date and time :{time.ctime()}\n") 
        
        print("Log Created Succesfully")
    

def main():
    directoryPath= input("Enter The Directory Path :")

    schedule.every(1).minute.do(DirectoryScan,directoryPath)  

    while(1):

        schedule.run_pending()
        time.sleep(45)



if __name__ =="__main__":
    main()