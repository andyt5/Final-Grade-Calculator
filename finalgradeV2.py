#finalgrade.py VERSION 2
#3/22/21
#Andy Tang
#This program allows an instructor to calculate the final grade for students in a class.



def main():
    #Declaring variables
    examGrade = 0
    examTotal = 0
    examAverage = 0
    homeworkTotal = 0
    quizTotal = 0
    quizGrade = 0
    homeworkGrade = 0
    optionSelect = 0
    #Introduction
    print("Grades will be calculated as follows: \nQuizzes: 40%\nExams: 40%\nHomework: 20%")
    while optionSelect !=2:
        print("\nPlease choose from the following menu: \n1) Enter new student information\n2) Exit")

        #Option Select
        optionSelect = int(input("\nEnter your choice here: "))

        #if they choose to enter student information
        if optionSelect == 1:
       
            print("\nYou have chosen to calculate the grade for a student.\n")

            quizWeight = float(input("How much do the quizzes weigh? "))/100
            examWeight = float(input("How much do the exams weigh? "))/100
            homeworkWeight = float(input("How much does the homework weigh? "))/100

            numExams = input("How many exams were given? ")

            #For amount of number of exams/quizzes/homework that they type in, iterate through the number given.
            for i in range(int(numExams)):
                examGrade = float(input("Enter exam grade: "))
                while examGrade < 0  or examGrade > 100:
                  
                    print("Invalid grade. Must be between 0 and 100.")
                   
                    examGrade = float(input("Enter exam grade: "))
                examTotal += int(examGrade)


            
            #if the number wasn't a negative, continue to find the average
            examAverage = int(examTotal)/int(numExams)
            print("\nAverage exam grade: " + str(examAverage))
        
            examTotal = 0
        

            #same system as number of exams but with quizzes
            numQuizzes = input("\nHow many quizzes were given? ")

            #same system as finding range for number of exams but with quizzes
            for i in range(int(numQuizzes)):
                quizGrade = float(input("Enter quiz grade: "))
                while quizGrade < 0 or quizGrade > 100:
                    print("Invalid grade. Must be between 0 and 100.")
                    quizGrade = float(input("Enter quiz grade: "))
                quizTotal += int(quizGrade)

            quizAverage = int(quizTotal)/int(numQuizzes)

            print("\nAverage quiz grade: " + str(quizAverage))
            quizTotal = 0

            #same system as number of exams but with homework
            numHomework = input("\nHow many homework assignments were given? ")

            #same system as finding range for number of exams but with homework
            for i in range(int(numHomework)):
                homeworkGrade = float(input("Enter homework grade: "))
                while homeworkGrade < 0 or homeworkGrade > 100:
                    
                    print("Invalid grade. Must be between 0 and 100")
                    homeworkGrade = float(input("Enter homework grade: "))
                homeworkTotal += int(homeworkGrade)


            homeworkAverage = int(homeworkTotal)/int(numHomework)
            print("\nAverage homework grade: " + str(homeworkAverage))
            homeworkTotal = 0
           

            finalAverage = (quizWeight*quizAverage)+(examWeight*examAverage)+(homeworkWeight*homeworkAverage)
            print("\nFinal average for the class is: %0.1f" %finalAverage)
        #if they chose number 2 as an option, let the program exit itself.
        elif int(optionSelect) == 2:
            print("You have exited.")
        else:
            print("Invalid.")


