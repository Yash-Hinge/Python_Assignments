import schedule
import os
import time 



def DirectoryScan(Directory):
    if(os.path.isdir(Directory)):
        Filenum=0
        SubDirectoryCnt =0
        for Folders,subfolders,files in os.walk(Directory):
            Filenum=Filenum +len(files)
            SubDirectoryCnt=SubDirectoryCnt+len(subfolders)
    
        print("Directory Name :",Directory)
        print("Total No.of Subfolders :",SubDirectoryCnt)
        print("Total No.of Files :",Filenum)
        print("Time of Scanning :",time.ctime())


    




def main():
    D_name = input("Enter The Directory address or name  to be Scanned :")

    schedule.every(1).minute.do(DirectoryScan,D_name)  

    while(1):

        schedule.run_pending()




if __name__ =="__main__":
    main()