import schedule 
import psutil
import time 
import sys


def ProcessInfo(Processname):
   

    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=["pid","name","username","status"])
        pname = info.get("name")
        if(Processname==pname):
            
            print(f"Process Id : {info.get("id")}")
            print(f"Process Name: {info.get("name")}")
            print(f"Userame: {info.get("username")}")
            print(f"Status of Process:{info.get("status")}")
            return 

    print("Process Not Found : Check case or Processname again")
    





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