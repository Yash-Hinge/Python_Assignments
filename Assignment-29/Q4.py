import hashlib
import os
import sys

def ChkSame(Filename1,Filename2):

    if(os.path.exists(Filename1)==False or os.path.getsize(Filename2)==False):
        return FileNotFoundError
    ret = False
    hobj = hashlib.md5()
    fobj1=open(Filename1,"rb")
    buffer=fobj1.read(1000)
    while(len(buffer)>0):
        hobj.update(buffer)
        buffer=fobj1.read(1000)
    ChkSum1= hobj.hexdigest()

    fobj2=open(Filename2,"rb")

    buffer = fobj2.read(1000)
    while(len(buffer)>0):
        hobj.update(buffer)
        buffer =fobj2.read(1000)

    checkSum2 =hobj.hexdigest()

    if ChkSum1==checkSum2:
        return True 

    else :
        return False

    

    





def main():
    
    if(len(sys.argv)!=3):
        print("Inavlid no.of command line arguments : python filename.py Src_filename Dest_filename")
    ret = ChkSame(sys.argv[1],sys.argv[2])

    if(ret!=True):
        print("Files are Same ...")

    else:
        print("Files are Not Same ...")






if __name__ =="__main__":
    main() 