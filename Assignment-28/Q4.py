import os

def FileCopy(SrcFilename,DestFilename):
    if(os.path.exists(SrcFilename)!=True):
        return FileNotFoundError
    else:
        Srcfobj = open(SrcFilename,"r")
        Destfobj = open(DestFilename,"w")
        SrcFileSize = os.path.getsize(SrcFilename)
        DestFilesize =os.path.getsize(DestFilename)

        while(DestFilesize<=SrcFileSize):
            Buffer = Srcfobj.read(1024)
            Destfobj.write(Buffer)
            DestFilesize= os.path.getsize(DestFilename)

            if not Buffer:
                break
        
            
        
        return True 
    

    
       





def main():
    
    FilenameX = input("Enter the name of the Source  file :")
    FilenameY = input("Enter the name of Destination File :")
    

    ret = FileCopy(FilenameX,FilenameY)
    
    if (ret ==True ):
        print("file copied succesfully.")

    elif(ret ==FileNotFoundError):
        print("File Does not Exists:",ret)

    else :
        print("File Copy unsuccesful.")

    


if __name__ =="__main__":
    main()

