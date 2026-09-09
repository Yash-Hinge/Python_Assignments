import pandas as pd 
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plot
from sklearn . metrics import accuracy_score,confusion_matrix,ConfusionMatrixDisplay,classification_report
from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.model_selection import train_test_split,StratifiedKFold,cross_val_score


border = "-"*100
def read_data():
    print(border)
    print(border)
    print("Initiating Data Extraction from file..........")
    print(border)
    print(border)
    
    Data = pd.read_csv("MarvellousInfosystems_PlayPredictor.csv")
    if(len(Data)!=0):
        print("Data Read Succesfully..........")
    else:
        print("Data Reading Unsuccesfull.......")
    print(border)
    

    return Data

def Data_EDA(Data):
    print(border)
    print(border)
    print("Initializing Data Explanatory Analysis..........")
    print(border)
    print(border)

    print("\n")
    print(border)
    print("Total Number of Rows and Columns in The DataSet :-")
    print(border)
    print(Data.shape)
    print(border)
    print("\n")

    print(border)
    print("Name of Columns in the DataSet :-")
    print(border)
    print((list(Data.columns)))
    print(border)
    print("\n")

    print(border)
    print("Datatype of each Column:-")
    print(border)
    print(Data.dtypes)
    print("\n")

    print(border)
    print("Number OF Elements in the DataSet:-")
    print(border)
    print(len(Data))
    print("\n")

    print(border)
    print("Initial Records of The DataSet :-")
    print(border)
    print(Data.head())
    print("\n")

    print(border)
    print("Description about the Data :-")
    print(border)
    print(Data.describe())

    wether_encoder = LabelEncoder()
    temprature_encoder = LabelEncoder()
    Encoded_Wether= wether_encoder.fit_transform((Data['Wether']))
    Encoded_Temperature = temprature_encoder.fit_transform(Data['Temperature'])
    print(border)
    print("Encoded Data(Wether) :-")
    print(border)
    print(Encoded_Wether)

    print(border)
    print("Encoded Data(Temperature) :-")
    print(border)
    print(Encoded_Temperature)

    DataX = Data
    DataX['Wether']= Encoded_Wether
    DataX['Temperature']=Encoded_Temperature

    for data in DataX:
        print(data)

    return DataX



def Train_Test_model(Data):
    print(border)
    print(border)
    print("Model Training instantiated............")
    print(border)
    print(border)
    
    independent_var = ['Wether','Temperature']
    dependent_var = 'Play'

    X=Data[independent_var]
    Y=Data[dependent_var]
    X_train,X_test,Y_train,Y_Test=train_test_split(X,Y,test_size=0.5,random_state=43,stratify=Y)
    print(border)
    print(border)
    print("Model Training instantiated............")
    print(border)
    print(border)

    Scaler =StandardScaler()
    X_Train_Scaled = Scaler.fit_transform(X_train)
    X_Test_Scaled = Scaler.transform(X_test)
    model = KNeighborsClassifier()

    model_f  = model.fit(X_Train_Scaled,Y_train)

  
    print("Model Trained Succesfully.......")
    print(border)



    print(border)
    print(border)
    print("Model Testing instantiated............")
    print(border)
    print(border)


    Y_pred = model.predict(X_Test_Scaled)

    print(border)
    print("Model Tested Succesfully....")
    print(border)
    cv = StratifiedKFold(n_splits=5,random_state=42,shuffle=True)
    print(border)
    print("Cross validation Score ..........")
    print(border)

    scores = cross_val_score(model,X=X_Train_Scaled,y=Y_train,cv=cv)
    print("Cross Validation Score :-")
    print(scores)
    print("\n")

    print("Mean CV Accuracy :-")
    print(scores.mean())
    print("\n")

    print("Standard Deviation:-")
    print(scores.std())
    print("\n")

    print(border)
    print("Accuracy Score....")
    print(border)


    model_accuracy= accuracy_score(Y_Test,Y_pred)
    print("Model accuracy is :-")
    print(model_accuracy*100)
    print(border)
    print("Confusion MAtrix")
    print(border)

    cm = confusion_matrix(Y_Test,Y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=['Yes','No'])

    disp.plot()
    plot.title("PlayPredict Confusion Matrix ")
    plot.show()

    print(border)
    print("Classification Report....")
    print(border)
    
    Report = classification_report(Y_Test,Y_pred,zero_division=0)
    print(Report)
def main():
    Data = read_data()
    Cleaned_Data= Data_EDA(Data)
    Train_Test_model(Cleaned_Data)

if __name__ =="__main__":
    main()