numbers = []

for i in range(1, 11):
    num = float(input(f"enter num{i}: "))
    numbers.append(num)

num1 = numbers[0]

for i in range(1, 10):
    result = num1 - sum(numbers[1:])

print(f"The answer is: {result}")