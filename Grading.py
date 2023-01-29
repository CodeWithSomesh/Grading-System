import os


def studentName():
    # Initialize Variables
    valid = True
    name = ""

    # Ask user for Student Name
    # Validate input
    while valid:
        name = input("Enter Student Name: ")
        if name.isalpha():
            return name
        else:
            print("Invalid Input, Please Key In The Correct Name")
            continue


def studentID():
    # Initialize Variables
    valid = True
    id = 0

    # Ask user for Student ID
    # Validate input
    while valid:
        id = input("Enter 8 - Digit Student ID: P")
        if id.isnumeric():
            if len(id) == 8:
                return id
            else:
                print("Invalid Length, Please Key In The Correct 8- Digit ID.")
                continue
        else:
            print("Invalid Input, Please Key In The Correct ID.")
            continue


def weightage():
    # Initialize variables
    valid = True
    testWeight = 0

    # Ask user for Test Weight
    # Validate input
    while valid:
        testWeight = input("Weight (0-100): ")
        if testWeight.isnumeric():
            testWeight = int(testWeight)
            if 0 <= testWeight <= 100:
                return testWeight
            else:
                print("Invalid Input, Please Key In The Correct Weight.")
                continue
        else:
            print("Invalid Input, Please Enter The Correct Weight")
            continue


def weightageValidation(test, finalExam, assignment):
    # Initialize Variables
    sumOfWeights = 0
    retry = 0

    # Calculate Sum of All Weightages
    sumOfWeights = test + finalExam + assignment

    # Validate Weightage, making sure its exactly 100
    while sumOfWeights!=100:
        print("Total Weightage Of All Assessment Should Be 100")
        print("Please Check Your Weightage Inputs and Try Again Later.")
        os.system("pause")
        os.system("cls")
        main()


def scoreEarned():
    # Initialize variables
    valid = True
    testScore = 0

    # Ask user for Test Score
    # Validate input
    while valid:
        testScore = input("Test Score: ")
        if testScore.isnumeric():
            testScore = int(testScore)
            if 0 <= testScore <= 100:
                return testScore
            else:
                print("Invalid Score, Please Key In The Correct Test Score.")
                continue
        else:
            print("Invalid Score, Please Key In The Correct Test Score.")
            continue


def wereScoreShifted():
    # Initialize Variables
    valid = True
    shiftScore = 0

    # Ask user for Shifted Score
    # Validate input
    while valid:
        shiftScore = input("Were Scores Shifted (1=Yes, 2=No): ")
        if shiftScore.isnumeric():
            shiftScore = int(shiftScore)
            if shiftScore == 1 or shiftScore == 2:
                return shiftScore
            else:
                print("Invalid Input, Please Enter 1 or 2 Only")
                continue
        else:
            print("Invalid Input, Please Enter 1 or 2 Only")
            continue


def shiftedScoreAmount(scoreShift):
    # Initialize Variables
    valid = True
    shiftedAmount = 0

    # Ask user for Shift Amount
    # Validate input
    if scoreShift == 1:
        while valid:
            shiftedAmount = input("Shift Amount: ")
            if shiftedAmount.isnumeric():
                shiftedAmount = int(shiftedAmount)
                if 1 <= shiftedAmount <= 100:
                    return shiftedAmount
                else:
                    print("Invalid Input, Please Enter The Correct Amount")
                    continue
            else:
                print("Invalid Input, Please Enter The Correct Amount")
                continue
    else:
        return shiftedAmount


def totalPoints(scorePoints, shiftedScore, shiftedAmount):
    # Initialize Variables
    totalPoints = 0

    # Calculate Total Points
    totalPoints = scorePoints + shiftedAmount

    # If Score is Not Shifted
    if shiftedScore == 2:
        totalPoints = scorePoints
        print(f"Total Points = {totalPoints}/100")
        return totalPoints
    # If Score is Not Shifted
    else:
        # Validate totalPoints to make sure it caps at 100 points
        if totalPoints > 100:
            totalPoints = 100
            print(f"Total Points = {totalPoints}/100")
        else:
            # Print Total Points
            print(f"Total Points = {totalPoints}/100")
        return totalPoints


def totalWeightedScore(weightage, totalPoints):
    # Initialize Variables
    weightedScore = 0

    # Calculate Weighted Score
    weightedScore = weightage * (totalPoints/100)
    print(f"Weighted Score = {weightedScore:.1f}/{weightage}")
    return weightedScore


def assignmentNum():
    # Initialize Variables
    valid = True
    numOfAssignments = 0

    # Ask user for Number of Assignments
    # Validate input
    while valid:
        numOfAssignments = input("Number of Assignments: ")
        if numOfAssignments.isnumeric():
            numOfAssignments = int(numOfAssignments)
            if numOfAssignments > 0:
                numOfAssignments = int(numOfAssignments)
                return numOfAssignments
            else:
                print("Invalid Input, Please Enter The Correct Number")
                continue
        else:
            print("Invalid Input, Please Enter The Correct Number")
            continue


def totalAssignmentMarks(numOfAssigments):
    # Initialize Variables
    assignmentScore = 0
    assignmentMax = 0
    totalAssignmentScore = 0
    totalAssignmentMax = 0
    totalAssignmentMarks = 0

    # Ask user for the Score of Each Assignment
    for i in range(1, numOfAssigments + 1):
        assignmentScore = int(input(f"Assignment {i} Score: "))
        assignmentMax = int(input(f"Assignment {i} Max: "))
        i += 1
        totalAssignmentScore += assignmentScore
        totalAssignmentMax += assignmentMax

    return (totalAssignmentScore,totalAssignmentMax)


def sectionAttended():
    # Initialize Variables
    valid = True
    attendedSection = 0


    # Ask user for Section Attended
    # Validate input
    while valid:
        attendedSection = input("How Many Sections Attended: ")
        if attendedSection.isnumeric():
            attendedSection = int(attendedSection)
            if attendedSection >= 0:
                return attendedSection
            else:
                print("Invalid Input, Please Key In The Correct Number Of Attended Sections")
                continue
        else:
            print("Invalid Input, Please Key In The Correct Number Of Attended Sections")
            continue


def sectionPoints(sectionsAttended):
    # Initialize Variables
    totalSectionPoints = 0
    SECTION_POINTS = 3

    # Calculate the Section Points
    totalSectionPoints = sectionsAttended * SECTION_POINTS

    # Print the total Section Points
    print(f"Section Points = {totalSectionPoints}/34")
    return totalSectionPoints


def calculateHomeworkPoints(totalAssignmentScore,totalAssignmentMax,totalSectionPoints):
    # Initialize Variables
    totalPoints = 0
    totalMaxPoints = 0
    TOTAL_SECTION_POINTS = 34

    # Calculate Total Points for Assignment
    totalPoints = totalAssignmentScore + totalSectionPoints
    # Calculate The Maximum Attainable Marks for Assignment
    totalMaxPoints = totalAssignmentMax + TOTAL_SECTION_POINTS

    #Validate Total Points at its Cap Limit
    if totalPoints > 100 and totalMaxPoints > 100:
        totalPoints = 100
        totalMaxPoints = 100
        print(f"Total Points = {totalPoints}/{totalMaxPoints}")
    elif totalMaxPoints > 100:
        totalMaxPoints = 100
        print(f"Total Points = {totalPoints}/{totalMaxPoints}")
    elif totalPoints > totalMaxPoints:
        totalPoints = totalMaxPoints
        print(f"Total Points = {totalPoints}/{totalMaxPoints}")
    else:
        print(f"Total Points = {totalPoints}/{totalMaxPoints}")
    return (totalPoints, totalMaxPoints)


def homeworkTotalWeightedScore(totalHomeworkScore, totalHomeworkMaxScore, weightage):
    # Initialize Variables
    weightedScore = 0

    #Calculate Weighted Score with given formula
    weightedScore = (totalHomeworkScore/totalHomeworkMaxScore) * weightage

    #Print Weighted Score
    print(f"Weighted Score = {weightedScore:.1f}/{weightage}")
    return weightedScore


def overallPercentage(testWeightedScore, finalExamWeightedScore, assignmentWeightedScore):
    # Initialize Variables
    overall = 0

    # Calculate Overall Percentage
    overall = testWeightedScore + finalExamWeightedScore + assignmentWeightedScore
    print(f"Overall Percentage = {overall:.1f}")
    return overall


def expectedGrade(overallPercentage):
    # Initialize Variables
    leastExpectedGrade = ""

    # Display Least Expected Grade
    if 90<=overallPercentage<=100:
        leastExpectedGrade = "A"
        print(f"Your grade will be at least: {leastExpectedGrade}")
    elif 80<=overallPercentage<=89.9:
        leastExpectedGrade = "B"
        print(f"Your grade will be at least: {leastExpectedGrade}")
    elif 70<=overallPercentage<=79.9:
        leastExpectedGrade = "C"
        print(f"Your grade will be at least: {leastExpectedGrade}")
    elif 60<=overallPercentage<=69.9:
        leastExpectedGrade = "D"
        print(f"Your grade will be at least: {leastExpectedGrade}")
    else:
        leastExpectedGrade = "F"
        print(f"Your grade will be at least: {leastExpectedGrade}")
    return leastExpectedGrade


def customMessage(expectedGrade, studentName):
    # Initialize Variables
    message = ""

    # Display Custom Message
    if expectedGrade=="A" :
        print(f"Excellent Work {studentName}. You Are In The Dean's List. Keep Up The Exceptional Work. ")
    elif expectedGrade=="B":
        print(f"Good Work {studentName}. You Just Have To Push Yourself A Little More.")
    elif expectedGrade=="C":
        print(f"You Should Put In More Efforts {studentName}, You Can Definitely Do It.")
    elif expectedGrade=="D":
        print(f"You Need To Work Very Hard {studentName}. Remember Diamonds Are Made Under Pressure.")
    else:
        print(f"Getting a bad grade isn’t the end of the world {studentName}. Work Harder Next Time.")



def displayReport(name, id, testScore, finalsScore, assignmentScore, totalScore, grade, remarks):
    print("-" * 38)
    print("\t\tSTUDENT RESULT REPORT")
    print("-" * 38)
    print(f"Student Name                : {name}")
    print(f"Student ID                  : {id}")
    print(f"Test Weighted Score         : {testScore:.1f}%")
    print(f"Final Exam Weighted Score   : {finalsScore:.1f}%")
    print(f"Assignment Weighted Score   : {assignmentScore:.1f}%")
    print(f"Overall Percentage          : {totalScore:.1f}%")
    print(f"Expected Grade              : {grade}")

def restartProgram():
    # Initialize Variables
    restart = ""

    # Ask User for input to whether restart or exit program
    while True:
        restart = input("Next grading [Y/N]: ")
        if restart.isalpha():
            restart = restart.upper()
            if restart == "Y":
                os.system("pause")
                os.system("cls")
                main()
            elif restart == "N":
                exit()
            else:
                print("Invalid Input, Please Key In The Correct Input.")
                continue
        else:
            print("Invalid Input, Please Key In The Correct Input.")
            continue



def main():
    #Declare and Initialize Variables

    #Student Details
    name = ""
    id = 0

    #Test Details
    testWeightage = 0
    testScore = 0
    testScoreShifted = 0
    testShiftedScoreAmount = 0
    testTotalPoints = 0
    testWeightedScore = 0

    #Final Exam Details
    finalExamWeightage = 0
    finalExamScore = 0
    finalExamScoreShifted = 0
    finalExamShiftedScoreAmount = 0
    finalExamTotalPoints = 0
    finalExamWeightedScore = 0

    #Homework Details
    homeworkWeightage = 0
    numOfAssignments = 0
    assignmentScore = 0
    assignmentMaxScore = 0
    studentAttendedSections = 0
    totalSectionPoints = 0
    homeworkPoints = 0
    maxHomeworkPoints = 0
    homeworkTotalPoints = 0
    homeworkWeightedScore = 0

    #Overall Grade Details
    studentOverallPercentage = 0
    studentExpectedGrade = ""
    remarks = ""
    restart = ""


    #Ask user for Student Name and Student ID
    print("Student: ")
    name = studentName()
    id = studentID()
    print("\n")

    #Ask user for student's Test Details
    print("Test: ")
    testWeightage = weightage()
    testScore = scoreEarned()
    testScoreShifted = wereScoreShifted()
    testShiftedScoreAmount = shiftedScoreAmount(testScoreShifted)
    testTotalPoints = totalPoints(testScore, testScoreShifted, testShiftedScoreAmount)
    testWeightedScore = totalWeightedScore(testWeightage,testTotalPoints)
    print("\n")

    # Ask user for student's Final Exam Details
    print("Final: ")
    finalExamWeightage = weightage()
    finalExamScore = scoreEarned()
    finalExamScoreShifted = wereScoreShifted()
    finalExamShiftedScoreAmount = shiftedScoreAmount(finalExamScoreShifted)
    finalExamTotalPoints = totalPoints(finalExamScore, finalExamScoreShifted, finalExamShiftedScoreAmount)
    finalExamWeightedScore = totalWeightedScore(finalExamWeightage, finalExamTotalPoints)
    print("\n")

    # Ask user for student's Homework Details
    print("Homework: ")
    homeworkWeightage = weightage()
    weightageValidation(testWeightage, finalExamWeightage, homeworkWeightage)
    numOfAssignments = assignmentNum()
    assignmentScore, assignmentMaxScore = totalAssignmentMarks(numOfAssignments)
    studentAttendedSections = sectionAttended()
    totalSectionPoints = sectionPoints(studentAttendedSections)
    homeworkPoints, maxHomeworkPoints = calculateHomeworkPoints(assignmentScore, assignmentMaxScore, totalSectionPoints)
    homeworkWeightedScore = homeworkTotalWeightedScore(homeworkPoints, maxHomeworkPoints, homeworkWeightage)
    print("\n")

    # Display Student's Overall Percentage, GradExpected Grade and Custom Message
    studentOverallPercentage = overallPercentage(testWeightedScore, finalExamWeightedScore, homeworkWeightedScore)
    studentExpectedGrade = expectedGrade(studentOverallPercentage)
    remarks = customMessage(studentExpectedGrade, name)
    print("\n")

    # Clear Screen to Display Report
    os.system("pause")
    os.system("cls")

    # Display Student Report
    displayReport(name, id, testWeightedScore, finalExamWeightedScore, homeworkWeightedScore, studentOverallPercentage, studentExpectedGrade, remarks)
    print("\n")

    # Ask User input to whether restart program or exit program
    restart = restartProgram()



main()



