import os

def readLineX(Filename):
    fobj = open(Filename,"r")
    Line_Read = list()
    while(fobj.tell()!=os.path.getsize(Filename)):

        ret=fobj.readline()
        Line_Read.append(ret)
        
        
    return Line_Read
    

    
       





def main():
    
    Filename = input("Enter the name of the file :")
    

    ret = readLineX(Filename)
    for Line in ret :
        print(Line)






if __name__ =="__main__":
    main()

