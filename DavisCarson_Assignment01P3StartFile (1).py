#Name: Carson Davis
#Class: INFO 1200
#Section: See syllabus, schedule, or Canvas course for section
#Professor: Sharp
#Date: 11:05, 01/23/2025
#Assignment #: 1
#By submitting this assignment, I declare that the source code contained in this assignment was written
#solely by me, unless specifically provided in the assignment. I attest that no part of this assignment,
#in whole or in part, was directly created by Generative AI, unless explicitly stated in the assignment
#instructions, nor obtained from a subscription service. I understand that copying any source code,
#in whole or in part, unless specifically provided in the assignment, constitutes cheating, and that
#I will receive a zero on this project if I am found in violation of this policy.



firstName = ('Carson Davis')
print('Hello, my name is ' + firstName)

varschool = 'Utah Valley University'
print('I go to ' + varschool)

credits = 3
classes = 6
totalcredits = credits + classes

print('If I take 6 classes this semester and all are three credits each I will be taking ' + str(totalcredits) + ' credits')

print('I would like to save money by taking this many credits.')

maxCredits = 12
costPerClass = 350
classFee = 20

totalCostPerSemester = totalcredits - maxCredits / credits * costPerClass + classFee

print('If classes are free after the' + str(maxCredits) + ' credits and each class cost $' + str (costPerClass) + ' plus an additional $' + str (classFee) + ' per class fee, I will be saving $' + str(totalCostPerSemester) + ' a semester.')

totalCostPerYear = totalCostPerSemester + 3

print('That is a wopping $' + str(totalCostPerYear) + 'a year!')

print('This was a very informative and worth while Python assignment!')
