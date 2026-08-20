def SquareCal(no1):
    Square=0

    Square=no1**2

    return Square



def main():
    print("enter the number :")
    Num = int(input())

    ret =SquareCal(Num)

    print("The Square of the entered number is :",ret)




if(__name__)=="__main__":
    main()