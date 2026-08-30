import schedule 
import time 
import os



def DisplayfileContent(Filepath):
    

    if(os.path.exists(Filepath)==False):
        return FileNotFoundError
    elif(os.path.getsize(Filepath)==0):
        return FileExistsError
    elif(os.access(Filepath,os.R_OK)==False):
        return PermissionError
    else:
        fobj =open(Filepath ,"r")
        ret = fobj.read()
        print(ret)





def main():
    Filepath = input("enter the filename or path :")

    schedule.every().minute.do(DisplayfileContent,Filepath)


    while(1):
        schedule.run_pending()
        time.sleep(6)




if __name__=="__main__":
    main()