import pandas as pan



def readCsv():
    
    Filepath="student_performance_ml.csv"
    data= pan.read_csv(Filepath)
    print("File Loaded Succesfully...")

    print("Initial Records of file :\n")
    print(data.head())

    print("Last Records of file :\n")
    print(data.tail())
    
    print("Total No.of Rows and Columns are :")
    print(data.shape)
    print("\n")
    print("Name of Columns Are : ")
    print(list(data.columns))
    print("\n")
    print("Datatypes of each Column are :")
    print(data.dtypes)
    print("\n")


def main():
    print("initialising Process...")

    readCsv()


if __name__ =="__main__":
    main()