def Cubecal(no1):
    Cube =0
    Cube = no1**3
    return Cube



def main():
    print("enter the number :")
    num =int(input())

    ret = Cubecal(num)

    print("the cube of the entered number is :",ret)




if(__name__)=="__main__":
    main()