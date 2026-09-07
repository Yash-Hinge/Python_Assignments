import pandas as pd 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,ConfusionMatrixDisplay,classification_report
from sklearn.model_selection import train_test_split,cross_val_score,StratifiedKFold
import matplotlib.pyplot as plt 
from sklearn.preprocessing import StandardScaler 


def readData(Location):
    Data = pd.read_csv(Location)

    return Data 

def Data_EDA(Data):
    print("-"*100)
    print("Initialising Data Analysis.....")
    print("-"*100)

    print("\n\n")
    
    print("Total Number of Rows and Columns in The DataSet :-")
    print("-"*50)
    print(Data.shape)
    print("-"*50)
    print("\n")
    print("Name of Columns in the DataSet :-")
    print("-"*50)
    print(list(Data.columns))
    print("-"*50)
    print("\n")
    print("Datatype of each Column is :-")
    print("-"*50)
    print(Data.dtypes)
    print("-"*50)
    print("\n")
    print("Count of Wine Samples in The DataSet :-")
    print("-"*50)
    print(len(Data))
    print("-"*50)   
    print("Average amount of alcohol :",Data["Alcohol"].mean())
    print("-"*50)
    print("\n")
    print("-"*50)
    print("Average amount of Malic acid :",Data["Malic acid"].mean())
    print("-"*50)
    print("\n")
    print("-"*50)
    print("Average amount of Ash :",Data["Ash"].mean())
    print("-"*50)
    print("\n")
    print("-"*50)
    print("Average amount of Alcalinity of ash :",Data["Alcalinity of ash"].mean())
    print("-"*50)
    print("\n")
    print("-"*50)
    print("Average amount of Magnesium :",Data["Magnesium"].mean())
    print("-"*50)
    print("\n")
    print("-"*50)
    print("Average amount of Total phenols :",Data["Total phenols"].mean())
    print("-"*50)
    print("\n")
    print("-"*50)
    print("Average amount of Flavanoids :",Data["Flavanoids"].mean())
    print("-"*50)
    print("\n")
    print("-"*50)
    print("Average amount of Nonflavanoid phenols :",Data["Nonflavanoid phenols"].mean())
    print("-"*50)
    print("\n")
    print("-"*50)
    print("Average amount of Proanthocyanins :",Data["Proanthocyanins"].mean())
    print("-"*50)
    print("\n")
    print("-"*50)
    print("Average amount of Color intensity :",Data["Color intensity"].mean())
    print("-"*50)
    print("\n")
    print("-"*50)
    print("Average amount of Hue :",Data["Hue"].mean())
    print("-"*50)
    print("\n")
    print("-"*50)
    print("Average amount of OD280/OD315 of diluted wines :",Data["OD280/OD315 of diluted wines"].mean())
    print("-"*50)
    print("\n")
    print("-"*50)
    print("Average amount of Proline :",Data["Proline"].mean())
    print("-"*50)
    print("\n")
    print("-"*50)
    print("Described Report of the Database: ")
    print(Data.describe())

    Data["Class"].value_counts().sort_index().plot(kind="bar")

    plt.title("Wine Class Distribution")
    plt.xlabel("Wine Class")
    plt.ylabel("Number of Samples")
    plt.xticks(rotation=0)
    plt.show()

        
    
    Data_Cleaned= Data.dropna()
    Data_Cleaned.to_csv("Cleaned_Dataset.csv",index=False)
    print("-"*50)
    print("Data CLeaned Succesfully........ ")
    print("-"*50)
    print("\n\n")
    return Data_Cleaned
    


def Data_Visualization(C_data):
##########################################################
# 
##########################################################
    print("-"*100)
    print("Initialising Data Visualization process .....")
    print("-"*100)

    print("-"*50)
    print("Alcohol v/s Class Scatter plot :-")
    print("-"*50)
    print("Description: This scatter plot shows the distribution of alcohol content across the three wine classes." \
    " It helps us observe whether different wine classes have distinguishable alcohol levels. ")
    plt.figure(figsize=(7,5))
    for res in C_data["Class"].unique():
        temp = C_data[C_data["Class"]==res]
        plt.scatter(temp["Alcohol"],temp["Class"],label =res )
    plt.title("Classification Based on Alcohol Contents :")
    plt.ylabel("Class")
    plt.xlabel("Alcohol")
    plt.grid()
    plt.legend()
    plt.show()
    print("-"*50)
    print("Description: This scatter plot shows the relationship between malic acid content and wine class. " \
        "It helps identify whether malic acid levels vary between the three wine classes.")
    print("Malic Acid v/s Class Scatter plot :-")
    print("-"*50)
    plt.figure(figsize=(7,5))
    for res in C_data["Class"].unique():
        temp = C_data[C_data["Class"]==res]
        plt.scatter(temp["Malic acid"],temp["Class"],label =res )
    plt.title("Classification Based on Malic Acid Contents :")
    plt.ylabel("Class")
    plt.xlabel("Malic Acid")
    plt.grid()
    plt.legend()
    plt.show()

    print("-"*50)
    print("Ash v/s Class Scatter plot :-")
    print("-"*50)
    print("Description: This scatter plot shows the distribution of ash content for each wine class." \
        " It helps us examine whether ash content can be used to distinguish between different wine classes.")
    plt.figure(figsize=(7,5))
    for res in C_data["Class"].unique():
        temp = C_data[C_data["Class"]==res]
        plt.scatter(temp["Ash"],temp["Class"],label =res )
    plt.title("Classification Based on Ash Contents :")
    plt.ylabel("Class")
    plt.xlabel("Ash")
    plt.grid()
    plt.legend()
    plt.show()

    print("-"*50)
    print("Alcalinity of Ash v/s Class Scatter plot :-")
    print("-"*50)
    print("Description: This scatter plot represents the alcalinity of ash for each wine class." \
        " It helps us observe differences in alcalinity values among the three wine classes.")
    plt.figure(figsize=(7,5))
    for res in C_data["Class"].unique():
        temp = C_data[C_data["Class"]==res]
        plt.scatter(temp["Alcalinity of ash"],temp["Class"],label =res )
    plt.title("Classification Based on Alcalinity of ash Contents :")
    plt.ylabel("Class")
    plt.xlabel("Alcalinity of ash")
    plt.grid()
    plt.legend()
    plt.show()

    print("-"*50)
    print("Magnesium v/s Class Scatter plot :-")
    print("-"*50)
    print("Description: This scatter plot shows the magnesium content across the three wine classes." \
    " It helps determine whether magnesium levels show noticeable differences between the classes.")
    plt.figure(figsize=(7,5))
    for res in C_data["Class"].unique():
        temp = C_data[C_data["Class"]==res]
        plt.scatter(temp["Magnesium"],temp["Class"],label =res )
    plt.title("Classification Based on Magnesium Contents :")
    plt.ylabel("Class")
    plt.xlabel("Magnesium")
    plt.grid()
    plt.legend()
    plt.show()

    print("-"*50)
    print("Total Phenols  v/s Class Scatter plot :-")
    print("-"*50)
    print("Description: This scatter plot shows the distribution of total phenols among the wine classes. " \
        "It helps us understand whether total phenol content provides separation between different classes.")
    plt.figure(figsize=(7,5))
    for res in C_data["Class"].unique():
        temp = C_data[C_data["Class"]==res]
        plt.scatter(temp["Total phenols"],temp["Class"],label =res )
    plt.title("Classification Based on Total phenols Contents :")
    plt.ylabel("Class")
    plt.xlabel("Total phenols")
    plt.grid()
    plt.legend()
    plt.show()

    print("-"*50)
    print("Flavanoids v/s Class Scatter plot :-")
    print("-"*50)
    print("Description: This scatter plot represents flavanoid content for each wine class. " \
        "It helps identify whether flavanoid levels differ significantly between the three classes.")
    plt.figure(figsize=(7,5))
    for res in C_data["Class"].unique():
        temp = C_data[C_data["Class"]==res]
        plt.scatter(temp["Flavanoids"],temp["Class"],label =res )
    plt.title("Classification Based on Flavanoids Contents :")
    plt.ylabel("Class")
    plt.xlabel("Flavanoids")
    plt.grid()
    plt.legend()
    plt.show()

    print("-"*50)
    print("Nonflavanoid phenols v/s Class Scatter plot :-")
    print("-"*50)
    print("Description: This scatter plot shows the distribution of nonflavanoid phenols across the wine classes. " \
        "It helps us examine whether this chemical property varies between different classes.")
    plt.figure(figsize=(7,5))
    for res in C_data["Class"].unique():
        temp = C_data[C_data["Class"]==res]
        plt.scatter(temp["Nonflavanoid phenols"],temp["Class"],label =res )
    plt.title("Classification Based on Nonflavanoid phenols Contents :")
    plt.ylabel("Class")
    plt.xlabel("Nonflavanoid phenols")
    plt.grid()
    plt.legend()
    plt.show()

    print("-"*50)
    print("Proanthocyanins v/s Class Scatter plot :-")
    print("-"*50)
    print("Description: This scatter plot shows the proanthocyanin content for each wine class. " \
        "It helps us observe the variation of this property and its potential usefulness in distinguishing wine classes.")
    plt.figure(figsize=(7,5))
    for res in C_data["Class"].unique():
        temp = C_data[C_data["Class"]==res]
        plt.scatter(temp["Proanthocyanins"],temp["Class"],label =res )
    plt.title("Classification Based on Proanthocyanins Contents :")
    plt.ylabel("Class")
    plt.xlabel("Proanthocyanins")
    plt.grid()
    plt.legend()
    plt.show()

    print("-"*50)
    print("Color Intensity v/s Class Scatter plot :-")
    print("-"*50)
    print("Description: This scatter plot shows the color intensity of wines across the three classes. " \
    "It helps us determine whether color intensity differs between wine classes.")
    plt.figure(figsize=(7,5))
    for res in C_data["Class"].unique():
        temp = C_data[C_data["Class"]==res]
        plt.scatter(temp["Color intensity"],temp["Class"],label =res )
    plt.title("Classification Based on Color intensity Contents :")
    plt.ylabel("Class")
    plt.xlabel("Color intensity")
    plt.grid()
    plt.legend()
    plt.show()

    print("-"*50)
    print("Hue v/s Class Scatter plot :-")
    print("-"*50)
    print("Description: This scatter plot represents the hue values for each wine class." \
    " It helps us observe whether differences in hue can help distinguish between the three wine classes.")
    plt.figure(figsize=(7,5))
    for res in C_data["Class"].unique():
        temp = C_data[C_data["Class"]==res]
        plt.scatter(temp["Hue"],temp["Class"],label =res )
    plt.title("Classification Based on Hue Contents :")
    plt.ylabel("Class")
    plt.xlabel("Hue")
    plt.grid()
    plt.legend()
    plt.show()

    print("-"*50)
    print("OD280/OD315 of diluted wines v/s Class Scatter plot :-")
    print("-"*50)
    print("Description: This scatter plot shows the OD280/OD315 values across the three wine classes. " \
    "It helps us examine whether this measurement provides a noticeable separation between the classes")
    plt.figure(figsize=(7,5))
    for res in C_data["Class"].unique():
        temp = C_data[C_data["Class"]==res]
        plt.scatter(temp["OD280/OD315 of diluted wines"],temp["Class"],label =res )
    plt.title("Classification Based on OD280/OD315 of diluted wines Contents :")
    plt.ylabel("Class")
    plt.xlabel("OD280/OD315 of diluted wines")
    plt.grid()
    plt.legend()
    plt.show()

    print("-"*50)
    print("Proline v/s Class Scatter plot :-")
    print("-"*50)
    print("Description: This scatter plot shows the distribution of proline content across the three wine classes. " \
    "It helps us identify whether proline levels differ between the classes and whether this feature may contribute to wine classification")
    plt.figure(figsize=(7,5))
    for res in C_data["Class"].unique():
        temp = C_data[C_data["Class"]==res]
        plt.scatter(temp["Proline"],temp["Class"],label =res )
    plt.title("Classification Based on Proline Contents :")
    plt.ylabel("Class")
    plt.xlabel("Proline")
    plt.grid()
    plt.legend()
    plt.show()

##########################################################################
#
##########################################################################
def Train_Test_Model(Data):
    print("Initialising Model Trainning Process......")
    Independent_Variables =["Alcohol","Malic acid","Ash","Alcalinity of ash","Magnesium","Total phenols","Flavanoids","Nonflavanoid phenols","Proanthocyanins","Color intensity","Hue","OD280/OD315 of diluted wines","Proline"]
    Depenedent_Variable = "Class"

    X= Data[Independent_Variables]
    Y= Data[Depenedent_Variable]

    X_train,X_test,Y_Train,Y_test = train_test_split(X,Y,test_size=0.3,random_state=42,stratify=Data["Class"])

    


    modelM = KNeighborsClassifier()
    Scaler = StandardScaler()
    X_train_Scaled = Scaler.fit_transform(X_train)
    X_Test_Scaled = Scaler.transform(X_test)

    model = modelM.fit(X_train_Scaled,Y_Train)
    print("-"*50)
    print("Model Trained Succesfully......")
    print("-"*50)
    Y_Pred = modelM.predict(X_Test_Scaled)

    print("-"*50)
    print("Model Tested Succesfully......")
    print("-"*50)


    CV = StratifiedKFold(n_splits=5,shuffle=True,random_state=42)
   
    Scores = cross_val_score(modelM,X=X_train_Scaled,y=Y_Train,cv=CV)
    
    print("-" * 50)
    print("Cross Validation Scores:")
    print(Scores)

    print("-" * 50)
    print("Mean CV Accuracy:", Scores.mean())

    print("-" * 50)
    print("CV Standard Deviation:", Scores.std())




    Accuracy =( accuracy_score(Y_test,Y_Pred)*100)

    print("-"*50)
    print("Model Accuracy :- \n", Accuracy)
    print("-"*50)

    cm= confusion_matrix(y_true=Y_test,y_pred=Y_Pred)
    disp =ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=[1,2,3])
    disp.plot()
    plt.title("Wine Classifer Confusion Matrix ")
    plt.show()


    print("-" * 50)
    print("Classification Report ")
    print("-" * 50)
    Report = classification_report(y_pred=Y_Pred,y_true=Y_test)
    print(Report)

def main():

   Data= readData("WinePredictor.csv")
   Cleaned_Data=Data_EDA(Data)
   Data_Visualization(Cleaned_Data)
   Train_Test_Model(Cleaned_Data)


if __name__ =="__main__":
    main()



