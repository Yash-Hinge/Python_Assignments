from ArithematicsX import Add , Sub , Multiplication ,Division



def main():

    no1 = int(input("Enter the number :"))
    no2 = int(input("Enter the number :"))

    ret = Add(no1,no2)
    print( "Sum is :",ret)
    ret = Sub(no1,no2)
    print( "Diff is :",ret)
    ret = Multiplication(no1,no2)
    print( "product  is :",ret)
    ret = Division(no1,no2)
    print( "division  is :",ret)





if __name__ == "__main__":
    main()