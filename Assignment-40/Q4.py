import pandas as pan
import matplotlib.pyplot as plt
import numpy as np
from sklearn.tree import DecisionTreeClassifier  as Dtclass
from sklearn.model_selection import train_test_split
from sklearn.metrics import (accuracy_score,confusion_matrix,classification_report,ConfusionMatrixDisplay)

def readCsv():
    
    Filepath="student_performance_ml.csv"
    data= pan.read_csv(Filepath)
    print("File Loaded Succesfully...")

    print("Initial Records of file :\n")
    print(data.head())

    print("Last Records of file :\n")
    print(data.tail())

    Data_EDA(data)
def Data_EDA(data):
    print("Total No.of Rows and Columns are :")
    print(data.shape)
    print("\n")
    print("Name of Columns Are : ")
    print(list(data.columns))
    print("\n")
    print("Datatypes of each Column are :")
    print(data.dtypes)
    print("\n")

    print("Count of Students in record :")
    print(len(data))
    CntPass=0
    CntFail=0
    FinalResult = data["FinalResult"]
    for i in FinalResult:
        if i ==1:
            CntPass+=1
        elif i ==0:
            CntFail+=1
    print("Count of Students Passed the exam :")
    print(CntPass)    
    print("Count of Students Failed the exam :")
    print(CntFail)

    print("Average Study Hours: \n",int(data["StudyHours"].mean()))
    print("Average Attendance: \n",int(data["Attendance"].mean()))
    print("Average PreviousScore: \n",int(data["PreviousScore"].mean()))
    print("Average Sleep Hours: \n",int(data["SleepHours"].mean()))

    
    print("Class Distribution [FinalResult]:\n1->pass\n0->fail\n\n",(data["FinalResult"].value_counts(normalize=True)*100))
    print("Since the differenc between percentage of passed students is not approximately equal , \nThe database is not balanced .")
    Data_Visualization(data)

def Data_Visualization(data):

    plt.figure(figsize=(7,5))
    for res in data["FinalResult"].unique():
        temp = data[data["FinalResult"]==res]
        plt.scatter(temp["FinalResult"],temp["StudyHours"],label =res)

    plt.title("student_performance_ml Case Study ")
    plt.xlabel("FinalResult")
    plt.ylabel("StudyHours")
    plt.legend()
    plt.grid()
    plt.show()

    plt.figure(figsize=(7,5))
    for res in data["FinalResult"].unique():
        temp = data[data["FinalResult"]==res]
        plt.scatter(temp["FinalResult"],temp["Attendance"],label =res)

    plt.title("student_performance_ml Case Study ")
    plt.xlabel("FinalResult")
    plt.ylabel("Attendance")
    plt.legend()
    plt.grid()
    plt.show()
    
    print("As we observe from the plot(StudyHours v/sFinalResult)and plot(attendance v/s FinalResult)\n Higher Study Hours and Higher Attendance increase the Chances of passing ")

    
    plt.hist(data["StudyHours"],color="blue",)
    plt.xlabel("No. of Observation")
    plt.ylabel("Time(hrs)")
    
    plt.show()
    print("The histogram shows the Study Time for all records \nwe can Observe the Study time for all")


    plt.figure(figsize=(7,5))
    for res in data["FinalResult"].unique():
        temp = data[data["FinalResult"]==res]
        plt.scatter(temp["StudyHours"],temp["PreviousScore"],label =res,)

    plt.title("student_performance_ml Case Study ")
    plt.xlabel("studyHours")
    plt.ylabel("PreviousResult")
    plt.legend()
    plt.grid()
    plt.show()

    plt.boxplot(data = data, x ="Attendance")
    plt.title("Attendance  Boxplot ")
    plt.show()
    column = data['Attendance']
    q1 = column.quantile(0.25)
    q3 = column.quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr


    outliers = data[(column < lower_bound) | (column > upper_bound)]

    print(f"Total outliers found: {len(outliers)}")
    print(outliers[['Attendance']])

    plt.figure(figsize=(7,5))
    for res in data["FinalResult"].unique():
        temp = data[data["FinalResult"]==res]
        plt.scatter(temp["FinalResult"],temp["AssignmentsCompleted"],label =res,)

    plt.title("student_performance_ml Case Study ")
    plt.xlabel("FinalResult")
    plt.ylabel("AssignmentsCompleted")
    plt.legend()
    plt.grid()
    plt.show()
    print("The Scatter plot shows linear realtionship between Assignment Completed and FinalResult. ")

    plt.figure(figsize=(7,5))
    for res in data["FinalResult"].unique():
            temp = data[data["FinalResult"]==res]
            plt.scatter(temp["FinalResult"],temp["SleepHours"],label =res,)
    
    plt.title("student_performance_ml Case Study ")
    plt.xlabel("FinalResult")
    plt.ylabel("SleepHours")
    plt.legend()
    plt.grid()
    plt.show()
    print("The Scatter plot shows linear realtionship between SleepHours and FinalResult. ")

    Train_Evaluate_Model(data)

def Train_Evaluate_Model(data):
    #########################################################
    #   MODEL WITH max_depth = None
    #########################################################
    print("Model Trainning insitiated Succesfully....")
    features =["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours"]

    x=data[features]
    y=data["FinalResult"]

    print("Shape of Independent Vriables :",x.shape)
    print("Shape of Dependent Variables :",y.shape)

    X_train,X_test,Y_train,Y_test = train_test_split(x,y,test_size=0.3,random_state=42)
    print("-"*100)
    print("Decision Tree Classifier (max_depth=None)")
    print("-"*100)

    model=Dtclass()
    model.fit(X=X_train,y=Y_train)
    print("Model Trained Succesfully.....")

    
    Y_pred = model.predict(X=X_test)
    print("Predicted Values :")
    print(Y_pred)
    print("Actual Values :")
    print(Y_test)

    accuracy_real= accuracy_score(y_true=Y_test,y_pred=Y_pred)
    print("Accuracy Of model is :\n",accuracy_real*100)

    
    cm = confusion_matrix(Y_test,Y_pred,labels=model.classes_)
    disp=ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=["0","1"])
    disp.plot()
    plt.show()
    print("Confusion Matrix Plotted Succesfully...")
    print("Predicted Positive and Actual Positive :")


    Y_t_pred=model.predict(X_train)
    Train_accuracy = accuracy_score(Y_train,Y_t_pred)
    print("Trainning Accuray :")
    print((Train_accuracy*100))
    Test_Accuracy =accuracy_score(y_true=Y_test,y_pred=Y_pred)
    print("Testing Accuracy:")
    print(Test_Accuracy*100)

#########################################################
#   MODEL WITH max_depth = 1
#########################################################


    print("-"*100)
    print("Decision Tree Classifier (max_depth=1)")
    print("-"*100)
    
    model2=Dtclass(max_depth=1)
    model2.fit(X=X_train,y=Y_train)
    print("Model Trained Succesfully.....")

    
    Y_pred = model2.predict(X=X_test)
    print("Predicted Values :")
    print(Y_pred)
    print("Actual Values :")
    print(Y_test)

    accuracy= accuracy_score(y_true=Y_test,y_pred=Y_pred)
    print("Accuracy Of model is :\n",accuracy*100)

    print("-"*100)
    print("Decision Tree Classifier (max_depth=3)")
    print("-"*100)
    
    model3=Dtclass(max_depth=3)
    model3.fit(X=X_train,y=Y_train)
    print("Model Trained Succesfully.....")
#########################################################
#   MODEL WITH max_depth = 1
#########################################################
    
    Y_pred = model3.predict(X=X_test)
    print("Predicted Values :")
    print(Y_pred)
    print("Actual Values :")
    print(Y_test)

    accuracy= accuracy_score(y_true=Y_test,y_pred=Y_pred)
    print("Accuracy Of model is :\n",accuracy*100)

###########################################
#   New Data Insertion
###########################################


    new_data = pan.DataFrame({
        "StudyHours":[6],
        "Attendance":[85],
        "PreviousScore":[66],
        "AssignmentsCompleted":[7],
        "SleepHours":[7]
    })
    new_predict = model.predict(new_data)
    print("Prediction =",new_predict[0])


###########################################
## MOdel important features :
###########################################
    importance_model =model.feature_importances_

    for i in range(len(importance_model)):
        print(f"feature :{features[i]}\t ,importane = {importance_model[i]}\n")
        if(importance_model[i]==1):
            print(f"{features[i]} contributes most in Final Result prediction ")


##########################################################################
##
##      Dropt the column"Sleephours"
##
###########################################################################
            
    data1 = data.drop("SleepHours",axis=1)

    print(list(data1.columns))
    print("Dropped Column : 'SleepHours'")
    featuresX =["StudyHours","Attendance","PreviousScore","AssignmentsCompleted"]
    x = data1[featuresX]
    y = data1["FinalResult"]

    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

    modelX= Dtclass()

    modelX=modelX.fit(x_train,y_train)

    y_prd = modelX.predict(x_test)

    accuracy =accuracy_score(y_test,y_prd)

    print("Accuracy of real model :",accuracy_real*100)
    print("accuracy  of the Column Dropped  model is :",accuracy*100)

##########################################################################
##
##   Train model only with StudyHours,Attendance
##
###########################################################################

    
    featuresX =["StudyHours","Attendance"]
    x = data[featuresX]
    y = data["FinalResult"]

    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

    modelX= Dtclass()

    modelX=modelX.fit(x_train,y_train)

    y_prd = modelX.predict(x_test)

    accuracy =accuracy_score(y_test,y_prd)

    print("Accuracy of real model :",accuracy_real*100)
    print("accuracy  of New model is :",accuracy*100)

##########################################################################
##
##   NEw Record Insertion
##
###########################################################################
    new_Data = pan.DataFrame(
    {"StudyHours": [7, 6, 7, 6, 8], "Attendance": [80, 78, 86, 91, 92]})
    
    new_predict=modelX.predict(new_Data)
    for i in new_predict:
        print("the predictions are :",new_predict[i])


def main():


    print("initialising Process...")

    readCsv()


if __name__ =="__main__":
    main()