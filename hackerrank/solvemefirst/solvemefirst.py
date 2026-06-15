def solveMeFirst(number1: int, number2: int) -> int:
    number1 = 1 if number1 < 1 else number1
    number2 = 1000 if number2 > 1000 else number2
    result = number1 + number2
    return result

num1 = int(input())
num2 = int(input())
res = solveMeFirst(num1,num2)
print(res)