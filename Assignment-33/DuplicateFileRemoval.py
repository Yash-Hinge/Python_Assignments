import schedule 
import time 
import os
import smtplib
import hashlib
import sys
from email.message import EmailMessage


def CalChecksum(Filename):
          
    hobj = hashlib.md5()
    
    
    fobj = open(Filename,"rb")
    Buffer = fobj.read(1000)
    while(len(Buffer)>0):
        hobj.update(Buffer)
        Buffer =fobj.read(1000)
                
    fobj.close()
    CheckSum=hobj.hexdigest()
            
    return CheckSum



def DeleteDuplicate(DirectoryName ,receiver):
    Ret = os.path.exists(DirectoryName)
    DuplicateFiles= dict() 
    if(Ret == True):
        Ret=os.path.isdir(DirectoryName)
    if(Ret==False):
            os.mkdir(DirectoryName)


    Timestamp = time.strftime("%d-%m-%Y_%H-%M-%S")
    Filename = os.path.join(DirectoryName+f"FileLog_{Timestamp}.log")

    for Folders,Subfolders , Files in os.walk(DirectoryName):
        for fname in Files:
            fname =os.path.join(Folders,fname)
            Valcheck = CalChecksum(fname)

            if Valcheck in DuplicateFiles:
                DuplicateFiles[Valcheck].append(fname)
            else:
                 DuplicateFiles[Valcheck]=[fname]

    logF = open(Filename,"a")
    logF.write("-"*100+"\n")
    logF.write("DUPLICATE FILE REMOVAL LOG "+"\n")
    logF.write("-"*100+"\n")
    logF.write(f"\n Log File Created at  :{time.ctime()}")
    logF.write("\n\n\n")
    logF.write("-"*100+"\n")
    logF.write("DUPLICATE FILES :-\n")
    

    for Valcheck in DuplicateFiles:
        if len(DuplicateFiles[Valcheck]) > 1:
            logF.write("-"*100+"\n")
            logF.write(f"ChechSum Value: {Valcheck}\n")
            value = DuplicateFiles.get(Valcheck)
            logF.write(f"Filename Associated with CheckSum :{value}\n")
            logF.write("-"*100+"\n")

    total_files = 0
    for files in DuplicateFiles.values():
        total_files += len(files)

    logF.write("-"*100+"\n")
    logF.write("-"*100+"\n")
    logF.write("DELETED FILES:-\n")
    logF.write("-"*100+"\n")
    logF.write("-"*100+"\n")
    total_DuplicateFiles=0
    
    for files in DuplicateFiles.values():
            if len(files)>1:
                total_DuplicateFiles += len(files)
    total_DuplicateFilesDeleted=0
    for Valcheck in DuplicateFiles:
        if len(DuplicateFiles[Valcheck]) > 1:
            for duplicatefiles in DuplicateFiles[Valcheck][1:]:
                tal_DuplicateFilesDeleted +=1
                logF.write(f"CheckSum:{Valcheck}\n")
                logF.write(f"Deleted Files :{duplicatefiles}\n")
                os.remove(duplicatefiles)
                
                logF.write("-"*100+"\n")

    logF.write("END OF LOG FILE \n")

    logF.write("-"*100+"\n")
    logF.write("-"*100+"\n")
    logF.close()

    fobj = open("MailBody.txt","w")
    fobj.write("Jay Ganesh,\n")

    fobj.write("The Duplicate File Removal Operation has been Completed Succesfully")
    fobj.write(f"Starting Time :{time.ctime()}")
    fobj.write(f"\n\nTotal Files Scanned :{total_files} \n")
    fobj.write(f"Total Duplicate Files :{total_DuplicateFiles}\n")
    fobj.write(f"Total Duplicate File Deleted:{total_DuplicateFilesDeleted}\n")
    fobj.write(f"Time of Deletion :{time.ctime()}")
    fobj.close()

    MailFiletoReceiver(Filename,receiver)
    

def MailFiletoReceiver(Filename,receiver ):

        mail = EmailMessage()
        mail["FROM"]= 'File Survilence System .'
        mail["TO"]=receiver
        mail["Subject"]=f"File Deletion Log File -{time.ctime()}"
        bodyobj = open("MailBody.txt","r")
        body =bodyobj.read()

        mail.set_content(body)

        attachment = open(Filename,"rb")
        data=attachment.read()
        name = attachment.name

        mail.add_attachment(data,maintype="text",subtype="plain",filename = name)
        smtp=smtplib.SMTP_SSL("smtp.gmail.com",465)
        smtp.login("y31503036@gmail.com","gdgy mcuq ipup xanw")
        smtp.send_message(mail)
        print("Mail Sent Succesfully....")
        smtp.quit()

def help():
     print("-"*100+"\n")
     print("Welcome to the Help Window of Duplicate File cleaner :- \n")
     print("-"*100+"\n")

     print("This application accepts the Directoryname from commandline argumnets ," \
     "scans the directory for duplicate files, keeps one file as it is and deletes the remanining files .")
     print("For usage guide use --u flag ")

def usage():
        print("-"*100+"\n")
        print("Welcome to the Usage Window of Duplicate File cleaner :- \n")
        print("-"*100+"\n")  

        print("Correct Sequence of Command line Arguments :-")
        print("python 'filename.py' Directoryname receiver's email.")
        print("     sys.argv[0]      sys.argv[1]        sys.argv[2]")
        print("sys.argv[1]:- Enter the Directory name which should be scanned for duplicate files .  ")
        print("sys.argv[2]:- Enter the Receivers email to whom the log file should be sent .")



def main():

    # Check number of arguments
    if len(sys.argv) == 2:

        # Help
        if sys.argv[1] in ("--h", "--H", "--help"):
            help()
            return

        # Usage
        elif sys.argv[1] in ("--u", "--U", "--usage"):
            usage()
            return

        
        else:
            print("Invalid number of command line arguments.")
            print("Use --h for help or --u for usage.")
            return

    
    if len(sys.argv) != 3:
        print("Invalid number of command line arguments.")
        print("Correct format:")
        print("python filename.py DirectoryName ReceiverEmail")
        return

    DirectoryName = sys.argv[1]
    Receiver = sys.argv[2]

    
    if "@" not in Receiver or "." not in Receiver:
        print("Error: Invalid email address.")
        return

    print("Arguments are valid.")
    print("Directory :", DirectoryName)
    print("Receiver  :", Receiver)

    schedule.every(1).hour.do( DeleteDuplicate,DirectoryName,Receiver)


    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ =="__main__":
     main()