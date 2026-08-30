

def CntLines(Filename):
    lineCnt=0
    
        

    fobj = open(Filename,"r")
 
    Lines = fobj.readlines()
    lineCnt=len(Lines)
    print(lineCnt)
    
    return lineCnt
       





def main():
    
    Filename = input("Enter the name of the file :")
    

    ret = CntLines(Filename)

    print("The number of lines in the given file is :",ret)






if __name__ =="__main__":
    main()

