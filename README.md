# Grading-System
Python Grading System (College Assignment)
----------------------------------------------------

## 📄Description of the Problem

Write a program to allow the academic staff to enter the coursework marks and final marks for 
the students. The program reads scores in three categories: test, assignments and final. Each 
category is weighted: its points are scaled up to a fraction of the 100 percent grade for the 
course. As the program begins reading each category, it first prompts for the category's weight.

</br>

The user begins by entering student id and name follows by the scores earned on test. The 
program asks whether test scores were shifted, interpreting an answer of 1 to mean “yes” and 
2 to mean “no.” If there is a shift, the program prompts for the shift amount, and the shift is 
added to the user's test score. Exam scores are capped at a max of 100; for example, if the user 
got 95 and there was a shift of 10, the score to use would be 100. The midterm's “weighted 
score” is printed, which is equal to the user's score multiplied by the exam's weight. Next, the 
program prompts for data about the final. The behavior for each is the same as the behavior 
for test.

</br>

Next, the user enters information about his/her homework, including the weight and how many 
assignments were given. For each assignment, the user enters a score and points possible. Use 
a cumulative sum as described in lecture. Part of the homework score comes from sections 
attended. We will simplify the formula to assume that each section attended is worth 3 points, 
up to a maximum of 34 points.

</br>

Once the program has read the user information for both exams and homework, it prints the 
student's overall percentage earned in the course, which is the sum of the weighted scores from 
the three categories, as shown below:

</br>

![image](https://user-images.githubusercontent.com/123357802/215338162-1a9ca2d9-0c4f-487f-9444-964457a1b0b9.png)

</br>

The program prints a loose guarantee about a minimum grade the student will get in the course, 
based on the following scale. See the logs of execution on the course web site to see the 
expected output for each grade range.

</br>

 90% and above: A; 89.99% - 80%: B; 79.99% - 70%: C; 69.99% - 60%: D; under 60%: F 
 
</br>
 
After printing the guaranteed minimum grade, print a custom message of your choice about the 
grade. This message should be different for each grade range shown above. It should be at 
least 1 line of any non-offensive text you like. Next, provide an option to repeat the next grading for the students with an appropriate prompt message.

</br>

You should handle the following two special cases of input:

</br>

⭐ A student can receive extra credit on an individual assignment, but the total points for 
homework are capped at the maximum possible. For example, a student can receive a 
score of 22/20 on one homework assignment, but if their total homework score for all 
assignments is 63/60, this score should be capped at 60/60. Section points are capped at 34.

</br>

⭐ Cap exam scores at 100. If the raw or shifted exam score exceeds 100, a score of 100 is 
used.

</br>

Otherwise, you may assume the user enters valid input. When prompted for a value, the user 
will enter an integer in the proper range. The user will enter a number of homework assignments ≥ 1, and the sum of the four weights will be exactly 100. The weight of each 
category will be a non-negative number. Exam shifts will be ≥ 0.

</br>

The program should be developed in a modular way using the functions, parameters, and 
returns value to eliminate redundancy. 

</br>

Give meaningful names to variables, and use proper indentation and whitespace. Follow 
Python’s naming standards as specified in lecture. Localize variables when possible; declare 
them in the smallest scope needed. Include meaningful comment headers at the top of your 
program and at the start of each function. Limit line lengths to 100 chars. Consider to use some 
customized functions to reduce the code redundancy and promote the code reusability.

</br>


![image](https://user-images.githubusercontent.com/123357802/215338216-dac86c6d-481c-4e49-b391-b6707bf63c4d.png)



