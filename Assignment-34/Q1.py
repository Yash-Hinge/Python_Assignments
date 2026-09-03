import schedule 
import psutil
import time 


def ProcessInfo():
    timestamp =time.strftime("%d-%m-%Y_%H-%M-%S")
    Filename = "ProcessLog"+timestamp
    fobj = open(Filename,"a")
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

    schedule.every(10).seconds.do(ProcessInfo)

    while(1):

        schedule.run_pending()
        time.sleep(1)



if __name__ =="__main__":
    main()