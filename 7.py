even = []

for i in range(1, 11):
    num = float(input(f"enter num{i}: "))
    if num % 2 == 0:
        even.append(num)
print("the even numbers are:", even)