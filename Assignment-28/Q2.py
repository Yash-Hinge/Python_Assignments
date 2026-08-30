import os

def CntWords(Filename):
    wordCnt=0
    
        

    fobj = open(Filename,"r")

    ret = fobj.read()
    words = ret.split()

    wordCnt=len(words)
    
    
    
    return wordCnt
       





def main():
    
    Filename = input("Enter the name of the file :")
    

    ret = CntWords(Filename)

    print("The number of words in the given file is :",ret)






if __name__ =="__main__":
    main()

