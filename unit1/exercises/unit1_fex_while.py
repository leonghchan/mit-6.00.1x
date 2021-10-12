"""
Exercise 1

Convert the following into code that uses a while loop
prints 2
prints 4
prints 6
prints 8
prints 10
prints Goodbye!
"""
num = 1
while num <= 10:
    if num % 2 == 0:
        print(num)
    num += 1
print("Goodbye!")


""" 
Exercise 2
Convert the following into code that uses a while loop
prints Hello!
prints 10
prints 8
prints 6
prints 4
prints 2
"""
num = 10
print("Hello!")
while num > 0:
    if num % 2 == 0:
        print(num)
    num -= 1

"""
Exercise 3
Write a while loop that sums the values 1 through end, inclusive. 
If end = 6. Then the answer will be 21 (1 + 2 + 3 + 4 + 5 + 6).
"""
end = 6
count = 0
result = 0

while count <= end:
    result += count
    count += 1
print(result)

