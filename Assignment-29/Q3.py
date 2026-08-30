import os 
import sys


def Copy_File(Src_Filename,Dest_Filename):

    if(os.path.exists(Src_Filename)==False):
        return FileNotFoundError
    ret = False
    srcfobj=open(Src_Filename,"r")
    destfobj=open(Dest_Filename,"w")
    Src_FilenameSize=os.path.getsize(Src_Filename)
    Dest_FilenameSize =os.path.getsize(Dest_Filename)
    while(Dest_FilenameSize<=Src_FilenameSize):
        ret = srcfobj.read(512)
        if(ret==""):
            break
        else:
            destfobj.write(ret)
            ret = True
    return ret

    

    





def main():
    
    if(len(sys.argv)!=3):
        print("Inavlid no.of command line arguments : python filename.py Src_filename Dest_filename")
    ret = Copy_File(sys.argv[1],sys.argv[2])

    if(ret!=True):
        print("File Copied Succesfuly......")

    else:
        print("File Copy Unsuccesful........")






if __name__ =="__main__":
    main() 