def chkDivisible5(No):
    if(No%5==0):
        return True
    
    else:
        return False


def main():

    Num = int(input("Enter The Number :"))
    ret = chkDivisible5(Num)

    if(ret==True):
        print("Divisible by 5")
    
    else:
        print("Not Divisible by 5")


if __name__ == "__main__":
    main()