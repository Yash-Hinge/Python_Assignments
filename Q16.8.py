def pattern(No):
    for i in range(No):
        print("*",end=" ")


def main():

    Num = int(input("Enter The Number :"))
    ret = pattern(Num)


if __name__ == "__main__":
    main()