def NaturalSum(no1):
    Sum =0
    for i in range(1,(no1+1)):
        Sum = Sum+i


    return Sum





def main():
    num = int(input("enter the number :"))

    ret = NaturalSum(num)
    print("the sum of first ",num,"Numbers is :",ret)





if(__name__)=="__main__":
    main()