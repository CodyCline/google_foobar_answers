#Acceptable solution using bitwise
def solution(num_str):
    num = int(num_str)
    ops = 0

    while(num != 1):
        if (num % 2 == 0):
            num = num / 2
        #If number is greater than 3 
        elif ((num == 3) or ((num + 1) & num) > ((num - 1) & (num - 2))):
            num -= 1
        else:
            num += 1
        ops += 1
    return ops

#My solution using math and logarithms which is not acceptable but achieves the same thing
import math
def math_solution(num): 
    operationCount = 0
    myNum = int(num)
    #If it can be divided by 2 
    while myNum != 1:
        if myNum % 2 == 0:
            myNum = myNum / 2
            operationCount += 1
        else: #If not a base-2 square root then round to closest
            closestNum = 2**(round(math.log(myNum, 2), 0))
            myNum = closestNum / 2
            operationCount += 1
    return operationCount