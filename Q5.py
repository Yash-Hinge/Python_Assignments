def Divisible3(no):

    if(no%3==0):
        return True
    else:
        return False
    



def main():
    print("Enter the number :")
    num = int(input())

    ret = Divisible3(num)

    if(ret==1):
        print("The number is divisible by 3")

    else:
        print("The number is not divisible by 3")




if(__name__)=="__main__":
    main()