import pandas as pd 
from sklearn.preprocessing import StandardScaler


def Read_Data():
    print("Data Reading Process Iniitiated Successfully.....")

    Data = pd.read_csv("Advertising.csv")

    return Data




def main():
    Data = Read_Data()      
    print("Data Read Succesfully...")



if __name__ =="__main__":
    main()