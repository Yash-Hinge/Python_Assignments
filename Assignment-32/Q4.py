import schedule 
import time 
import os
import shutil




def CopyTxtfile(SrcDirectorypath,DestDirectoryPath):
    if(os.path.isdir(SrcDirectorypath)==False):
        return NotADirectoryError("source directory not present .")
    if(os.path.isdir(DestDirectoryPath)==False):
            return NotADirectoryError("Destination directory not present .")
    fobj = open("FileCopyLog","a")
    for folder,subfolder,files in os.walk(SrcDirectorypath):
         for fname in files :
              SrcFileName = os.path.join(folder,fname)
              if(SrcFileName.endswith(".txt")):
                
                shutil.copy(SrcFileName,DestDirectoryPath)
                
                fobj.write("-"*100)
                fobj.write("\n")
                fobj.write("File log :")
                fobj.write("\n")
                fobj.write("-"*100)
                fobj.write("\n")
                fobj.write("Files Copied :-\n")
                fobj.write("\n")
                fobj.write(fname)
                fobj.write("\n")

    print("File Copy Success")




    

def main():
    SrcDirectorypath = input("enter the Source Directory name or path :")
    DestDirectoryPath= input("Enter the Destination Directory Path or name ")

    schedule.every(10).minutes.do(CopyTxtfile,SrcDirectorypath,DestDirectoryPath)


    while(1):
        schedule.run_pending()
        time.sleep(6)




if __name__=="__main__":
    main()