import schedule 
import time 



def createfile():
    timestamp = str(time.ctime())
    timestamp =timestamp.replace(" ","_")
    timestamp =timestamp.replace(":","-")

    filename= "File"+timestamp
    fobj =open(filename ,"w")
    fobj.write(filename)
    fobj.write(time.ctime())
    print("File Created Succesfully...")





def main():

    schedule.every(1).minute.do(createfile)


    while(1):
        schedule.run_pending()
        time.sleep(45)




if __name__=="__main__":
    main()