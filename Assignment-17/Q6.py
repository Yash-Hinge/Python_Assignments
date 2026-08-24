def pattern(No1):

    for i in range (No1,0,-1):
        for j in range(i):
            print("*",end="\t")
        print("\n")



def main():

    no = int(input("enter the number :"))

    pattern(no)




if __name__ =="__main__":
    main()