import pandas as pd 
from sklearn.preprocessing import StandardScaler


def Read_Data():
    print("Data Reading Process Iniitiated Successfully.....")

    Data = pd.read_csv("Advertising.csv")

    return Data

def EDA(Data):
    Border =  "-"*50
    print(Border)
    print ("Data Analysis :")
    print(Border)

    print(Border)
    print("Shape of DataSet :")
    print(Border)
    print(Data.shape)
    
    print(Border)
    print("Numbeer of elements In the DataSet:")
    print(Border)
    print(len(Data))

    print(Border)
    print("Name of Columns in the DataSet: ")
    print(Border)
    print(list(Data.columns))

    print(Border)
    print("Datatypes of Columns in the DataSet: ")
    print(Border)
    print(list(Data.dtypes))

    print(Border)
    print("Initial Records of the DataSet:")
    print(Border)
    print(Data.head())

    print(Border)
    print("Damaged or Empty Data Fregments of the Datset: ")
    print(Border)
    
    NUll_elements=Data[Data.isna().all(axis=1)]
    if(NUll_elements is None):
        print("No Damaged Data elements present ")

    else :
        print(NUll_elements)


    print(Border)
    print("Detailed Description of the Dataset")
    print(Border)
    print(Data.describe())
    print(Border)



def main():
    Data = Read_Data()      
    print("Data Read Succesfully...")
    C_Data=EDA(Data)


if __name__ =="__main__":
    main()