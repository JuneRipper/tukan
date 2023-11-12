x = int(input("Please enter a four-digit number: "))

first = x // 1000
second = x // 100 % 10
third = x // 10 % 10
fourth = x % 10

print(first)
print(second)
print(third)
print(fourth)



