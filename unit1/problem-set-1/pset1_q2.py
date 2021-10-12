"""
Pset 1 - Problem 2

Assume s is a string of lower case characters. 

Write a program that prints the number of times the string 'bob' occurs in s. For example, 
if s = azcbobobegghakl' your program should print 2. 
"""

from abc import abstractmethod


s = "bobbbobobbobbobobbobbbbobobooobobbobbcoobbofkobob"

# iterate through each letter.
# if  s[x: x+3] == 'bob' add 1 to count

result = 0
for i in range(len(s)):
    if s[i : i + 3] == "bob":
        result += 1
print(f"Number of times bob occurs is: {result}")

