import pandas as pd
import matplotlib.pyplot as plt
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
    data['Total']= (data['Math']+data['English']+data['Science'])
    print(border)
    print("Updated DataFrame :-")
    print(border)
    print(data)
    print("\n")

    print(border)
    print("Score in Science greater than 85 :- ")
    print(border)

    print(data[data['Science']>85])

    
    print(border)
    print("Updated Data:-")
    print(border)

    data['Name']=data['Name'].replace("Pooja","Puja")
    print(data)


    print(border)
    print("Sorted Data in Descending Order by total-")
    print(border)

    print(data.sort_values('Total',ascending=False))
          
    plt.bar(data['Name'],data['Total'],width=0.5)
    plt.xlabel("Student Name")
    plt.ylabel("Total Marks")
    plt.title("Total Marks v/s Student Name ")
    plt.show()

    Student = data[data['Name']=='Amit']
    Subject_performance = ["Math","English","Science"]

    plt.plot(Subject_performance,Student[Subject_performance].iloc[0],marker='o')
    plt.xlabel("Subjects")
    plt.ylabel("Performance in subjects ")
    plt.title("Amit's Performance ")
    plt.show()
    

def main():
    data()



if __name__ =="__main__":
    main()