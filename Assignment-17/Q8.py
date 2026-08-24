def pattern(No1):

    for i in range (No1):
        for j in range(1,(i+2)):
            print(j,end="\t")
        print("\n")



def main():

    no = int(input("enter the number :"))

    pattern(no)




if __name__ =="__main__":
    main()