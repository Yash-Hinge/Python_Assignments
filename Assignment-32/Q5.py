import schedule 
import time 
import os
import shutil




def CleanDirectory(Directorypath):
    if(os.path.isdir(Directorypath)==False):
        return NotADirectoryError("Directory not present .")

    
    fobj = open("DirectoryCleanLog.txt","a")
    fobj.write("-"*100)
    fobj.write("\n")
    fobj.write("File log :")
    fobj.write("\n")
    fobj.write("-"*100)
    fobj.write("\n")
    fobj.write("Files Deleted :-\n")
    for folder,subfolder,files in os.walk(Directorypath):
         for fname in files :
                FileName = os.path.join(folder,fname)
                if(os.access(FileName,os.R_OK)==True):

                    if(os.path.getsize(FileName)==0):
                        fobj.write("\n")
                        fobj.write(FileName)
                        fobj.write("\n")
                        os.remove(FileName)

                else:
                    return PermissionError("File Cannot be read ",FileName)
                

    print("Files Deleted  Successfully")




    

def main():
    Directorypath = input("enter the Source Directory name or path :")
    

    schedule.every(10).seconds.do(CleanDirectory,Directorypath)


    while(1):
        schedule.run_pending()
        time.sleep(1)




if __name__=="__main__":
    main()