import pandas as pd 
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,mean_squared_error,mean_absolute_percentage_error
import seaborn as sns 
import matplotlib.pyplot as plt 
Border =  "-"*50
def Read_Data():
    print("Data Reading Process Iniitiated Successfully.....")

    Data = pd.read_csv("Advertising.csv")
    Data= Data.drop(columns=['Unnamed: 0'])
    return Data

def EDA(Data):
    
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
    if NUll_elements.empty:
        print("No Damaged Data elements present ")

    else :
        print(NUll_elements)


    print(Border)
    print("Detailed Description of the Dataset")
    print(Border)
    print(Data.describe())
    print(Border)


    plt.figure(figsize=(8,6))
    sns.heatmap(Data.corr(numeric_only=True), annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.show()

    plt.figure(figsize=(6,4))
    plt.scatter(Data["TV"], Data["sales"])
    plt.xlabel("TV Advertising")
    plt.ylabel("Sales")
    plt.title("TV Advertising vs Sales")
    plt.show()

    plt.figure(figsize=(6,4))
    plt.scatter(Data["radio"], Data["sales"])
    plt.xlabel("radio Advertising")
    plt.ylabel("Sales")
    plt.title("radio Advertising vs Sales")
    plt.show()
    plt.figure(figsize=(6,4))
    plt.scatter(Data["newspaper"], Data["sales"])
    plt.xlabel("newspaper Advertising")
    plt.ylabel("Sales")
    plt.title("newspaper Advertising vs Sales")
    plt.show()

    print(Border)
    print("Independent And Dependent Variables")
    print(Border)
    X= Data.drop(columns="sales")
    Y =Data['sales']
    print("Independent Variables :", X)
    print("Dependent Variables :",Y)
    print("Shape of Independent Variables :",X.shape)
    print("Shape of Dependent Variables : ",Y.shape)

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3,random_state=42)

    Scalar = StandardScaler()
    X_train_Scaled=Scalar.fit_transform(X_train)
    X_test_Scaled= Scalar.transform(X_test)     

    return X_train_Scaled,X_test_Scaled,Y_train,Y_test

def Train_Test_Model(X_train,X_test,Y_train,Y_test):
    model = LinearRegression()
    print(Border)
    print("MOdel tainning initiated... ")
    print(Border)

    f_Data = model.fit(X_train,Y_train)
    print(Border)
    print("Model Trained Succesfully ")
    print(Border)
    Y_Train_pred= model.predict(X_train)
    print("Trainning Accuracy :-",(r2_score(Y_train,Y_Train_pred)*100))
    print("Actual trainning Outputs :-\n",Y_train)
    print("Predicted trainning Outputs:-\n",Y_Train_pred)
    print(Border)
    print("Model Testing initiated..")
    print(Border)

    Y_pred = model.predict(X_test)

    plt.figure(figsize=(6,4))
    plt.scatter(Y_test, Y_pred)

    plt.xlabel("Actual Sales")
    plt.ylabel("Predicted Sales")
    plt.title("Actual vs Predicted Sales")
    plt.show()
  
    r2_Score = r2_score(Y_test,Y_pred)
    print("Testing Accuracy:-", r2_Score*100)
    print("Actual testing  Outputs :-\n",Y_test)
    print("Predicted testing Outputs:-\n",Y_pred)

    print(Border)
    print("Error Calculation :-")
    print(Border)

    MSE = mean_squared_error(Y_test,Y_pred)
    print("Men Squared Error :-",MSE)
    MAPE = mean_absolute_percentage_error(Y_test,Y_pred)*100
    print("MEan Absolute Percentage Error :-",MAPE)


def main():
    Data = Read_Data()      
    print("Data Read Succesfully...")
    X_Split1,X_Split2,Y_Split1,Y_Split2=EDA(Data)
    Train_Test_Model(X_Split1,X_Split2,Y_Split1,Y_Split2)


if __name__ =="__main__":
    main()