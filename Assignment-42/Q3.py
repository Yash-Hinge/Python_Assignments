import math
def Calc__Euclidian_dist(point_1,point_2):

    dist = math.sqrt(((point_1['StudyHours']-point_2['StudyHours'])**2)+((point_1['Attendance']-point_2['Attendance'])**2))
    return dist 



def KNNClassifier_user_defined(x,y,k=3):
    border = "-"*50

    DataSet = [
            {"StudyHours":2,"Attendance":60,"Result":"Fail"},
            {"StudyHours":5,"Attendance":80,"Result":"Pass"},
            {"StudyHours":6,"Attendance":80,"Result":"Pass"},
            {"StudyHours":1,"Attendance":50,"Result":"Fail"}
            ]


    print(border)
    print("KNNClassifier_user_defined-")
    print(border)
    print(border,"\n")
    print("Classification Initiallising...")
    print(border,"\n" )

    print(border)
    print("DATASET:-")
    print(border,"\n")

    print(border)
    for element  in DataSet :
        print(element)

    print(border,"\n")

    newpoint={'StudyHours':x,'Attendance':y}

    for element in DataSet :
        element['Distance']= Calc__Euclidian_dist(element,newpoint)

    
    print(border)
    print("Distance of Given point from Data element and their Labels :")
    print(border)

    for element in DataSet:
        print(element['Distance'],"\t",element['Result'])



    Sorted_DataSet = sorted(DataSet,key = lambda item : item['Distance'])
    print(border )
    print("Sorted Dataset on basis of Distance from Given Point :-")
    print(border)

    for element in Sorted_DataSet:
        print(element)
    
    
    nearest_element = Sorted_DataSet[:k]

    print(border)
    print("Nearest Neighbours are :-")
    print(border)
    for ele in nearest_element:
        print(ele,"\n")

    
    Votes={}

    for neighbour_element in nearest_element:
        Result = neighbour_element['Result']
        Votes[Result] = Votes.get(Result,0)+1

    print(border)        
    print("Voting Result is :-")
    print(border)

    for d in Votes :
        print("label :",d,"\t","No.ofVotes :",Votes[d])

    iMax=0

    Name ="" 
    for VoteCnt in Votes:
        if Votes[VoteCnt]>iMax:
            iMax= Votes[VoteCnt]
            Name= VoteCnt 
            

    print("The PRedicted Output is :- ",Name)

def main():
    x=int(input("Enter the Study Hours of the Student :-   "))
    y= int(input("Enter the Attendance of the Student :-  "))
    KNNClassifier_user_defined(x,y,k=3) 



if __name__ == "__main__":
    main()
