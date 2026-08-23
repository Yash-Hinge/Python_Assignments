def CalCircleArea(Radius,PI=3.14):
    area = PI*(Radius*Radius)

    return area 




def main():
    radius = int(input("enter the radius:"))
   

    ret = CalCircleArea(radius)

    print("the area of the rectangle is :",ret)



if(__name__)=="__main__":
    main()