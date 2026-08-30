import os 


def Srch_File(Filename):

    if(os.path.exists(Filename)):
        return True 

    else :
        return False





def main():
    FileName = input("enter the file name :")

    ret = Srch_File(FileName)

    if(ret==True ):
        print("File Found : The file is present in current directory .")

    else:
        print("File Not Found : The file is not present in the current directory . ")





if __name__ =="__main__":
    main() 