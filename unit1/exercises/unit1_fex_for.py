"""
Exercise 1

Convert the following into code that uses a for loop
prints 2
prints 4
prints 6
prints 8
prints 10
prints Goodbye!
"""

for i in range(2, 11, 2):
    print(i)
print("Goodbye!")

""" 
Exercise 2
Convert the following into code that uses a for loop
prints Hello!
prints 10
prints 8
prints 6
prints 4
prints 2
"""

print("Hello!")
for i in range(10, 0, -2):
    print(i)

"""
Exercise 3
Write a for loop that sums the values 1 through end, inclusive. 
If end = 6. Then the answer will be 21 (1 + 2 + 3 + 4 + 5 + 6).
"""

end = 6
result = 0
for i in range(1, end + 1):
    result += i
print(result)
