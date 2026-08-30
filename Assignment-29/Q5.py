import os 


def search(Filename,srch_element):
    ElementCnt =0
    fobj = open(Filename,'r')
    words = list()
    ret = None
    Filesize=os.path.getsize(Filename)
    readsize=0
    
    while(readsize !=Filesize):
        ret =fobj.readline ()
        if(ret ==""):
            break

        words =ret.split(" ")

        for w in words :
            if srch_element == w:
                
                ElementCnt=ElementCnt+1        

        

    return ElementCnt

def main():

    Filename = input("Enter the name of the file :")

    serach_element = input("Enter the String to be searched :")

    ret = search(Filename,serach_element)

    if(ret >0 ):
        print("String Found .\n"+"No.of elemnts :",ret)

    else :
        print("String not Found .\n"+"No.of elemnts :",ret)




if __name__ =="__main__":
    main()