def disGrades(marks):
 
 if(marks>=75 and marks<=100):
    return "Distinction"
 
 elif(marks>=60 and marks<75):
    return "First Class"
 elif(marks>=50 and marks<60):
    return "Second Class"
 
 else:
    return "Fail"





def main():
    Num = int(input("enter the Marks:"))
   

    ret = disGrades(Num)

    print("Grades Scored :",ret)




if(__name__)=="__main__":
    main()