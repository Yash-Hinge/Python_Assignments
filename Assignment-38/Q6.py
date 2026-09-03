import pandas as pan
import matplotlib.pyplot as plt



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
    features =["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours"]

    X=data[features]
    y=data["FinalResult"]

    print("Shape of Independent Vriables :",X.shape)
    print("Shape of Dependent Variables :",y.shape)

    plt.figure(figsize=(7,5))
    for res in data["FinalResult"].unique():
        temp = data[data["FinalResult"]==res]
        plt.scatter(temp["StudyHours"],temp["FinalResult"],label =res)

    plt.title("student_performance_ml Case Study ")
    plt.xlabel("StudyHours")
    plt.ylabel("FinalResult")
    plt.legend()
    plt.grid()
    plt.show()

    plt.figure(figsize=(7,5))
    for res in data["FinalResult"].unique():
        temp = data[data["FinalResult"]==res]
        plt.scatter(temp["Attendance"],temp["FinalResult"],label =res)

    plt.title("student_performance_ml Case Study ")
    plt.xlabel("Attendance")
    plt.ylabel("FinalResult")
    plt.legend()
    plt.grid()
    plt.show()
    
    print("As we observe from the plot(StudyHours v/sFinalResult)and plot(attendance v/s FinalResult)\n Higher Study Hours and Higher Attendance increase the Chances of passing ")

    
    plt.hist(data["StudyHours"],color="blue",)
    plt.xlabel("No. of Observation")
    plt.ylabel("Time(hrs)")
    
    plt.show()
    print("The histogram shows the Study Time for all records \nwe can Observe the Study time for all")


   
def main():

    print("initialising Process...")

    readCsv()


if __name__ =="__main__":
    main()