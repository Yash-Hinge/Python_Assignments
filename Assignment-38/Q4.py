import pandas as pan




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
    



def main():
    print("initialising Process...")

    readCsv()


if __name__ =="__main__":
    main()