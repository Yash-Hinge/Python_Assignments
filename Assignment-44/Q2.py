import pandas as pd
def data():
    data =pd.DataFrame(
    {'Name':['Amit','Sagar','Pooja'],
         'Math':[85,90,78],
         'English':[75,85,82],
         'Science':[92,88,80]})

    border = "-"*50

    print(border)
    print("General Description :-")
    print(border)         

    print(border)
    print("Shape of DAtaFrame:")
    print(border)
    print(data.shape)
    print("\n")
    print(border)
    print("Column Name :-")
    print(list(data.columns))
    print(border)
    print("\n")
    print(border)
    print("Datatypes of Columns :-")
    print(data.dtypes)
    print(border)

    print(border)
    print("Detailed Description:- ")
    print(border)
    print(data.describe())
    print("\n")
    

def main():
    data()



if __name__ =="__main__":
    main()