def CalRectArea(len,wid):
    return len*wid




def main():
    length = int(input("enter the length:"))
    width = int(input("enter the width :"))

    ret = CalRectArea(length,width)

    print("the area of the rectangle is :",ret)



if(__name__)=="__main__":
    main()