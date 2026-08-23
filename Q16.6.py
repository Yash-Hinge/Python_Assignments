def chkNum(No):
    if(No>0):
        return 1
    elif(No<0):
        return -1
    
    else:
        return 0


def main():

    Num = int(input("Enter The Number :"))
    ret = chkNum(Num)

    if(ret==1):
        print("positive Number")
    elif(ret==-1):
        print("Negative Number")
    else:
        print("Zero")


if __name__ == "__main__":
    main()