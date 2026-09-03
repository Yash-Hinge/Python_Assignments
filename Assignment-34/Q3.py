import schedule 
import psutil
import time 
import sys
import os


def ProcessInfo(Directoryname):

    ret =os.path.exists(Directoryname)
    if(ret == True ):
        ret=os.path.isdir(Directoryname)
        if(ret == False):
            print("No such Directory found ")


            

    else:
        os.mkdir(Directoryname)
        
        
    timestamp =time.strftime("%d-%m-%Y_%H-%M-%S")
    Filename = os.path.join(Directoryname,f"Process_Log_File_{timestamp}.log")
    fobj=open(Filename,"a")
    
    
    fobj.write("-"*100+"\n")
    fobj.write(f"Process Log File \n Created at time :{time.ctime()}\n")
    fobj.write("-"*100+"\n")

    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=["pid","name","username"])
        fobj.write("-"*100+"\n")
        
        fobj.write("\n")
        fobj.write(f"Process Id : {info.get("pid")}\n")
        fobj.write(f"Process Name : {info.get("name")}\n")
        fobj.write(f"Username: {info.get("username")}\n")
        
        fobj.write("-"*100+"\n")

    fobj.write("-"*100+"\n")
    fobj.write("-"*100+"\n")
    fobj.write("End of Log File\n")
    fobj.write("-"*100+"\n")
    fobj.write("-"*100+"\n")

    print("Log File Created Sucsessfully")
    fobj.close()





def main():
    if(len(sys.argv)==2):
        schedule.every(10).seconds.do(ProcessInfo,sys.argv[1])

        while(1):

            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid no.of Arguments \n Enter thecorrect no.of arguments")



if __name__ =="__main__":
    main()