import os 



def Display_File(Filename):

    if(os.path.exists(Filename)==False):
        return FileNotFoundError

    fobj=open(Filename,"r")

    ret = fobj.read()

    return ret 

    





def main():
    FileName = input("enter the file name :")

    ret = Display_File(FileName)

    if(ret!=""):
        print("The Contents of the File are :\n",ret)






if __name__ =="__main__":
    main() 