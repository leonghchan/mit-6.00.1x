"""
Pset1 - Problem 1

Assume s is a string of lower case characters.
Write a program that counts up the number of vowels contained in the string s.
Do not define own values. 
"""

s = "azcbobobegghakl"
vowels_count = 0

for char in s:
    if char in ("a", "e", "i", "o", "u"):
        vowels_count += 1
print(f"Number of vowels: {vowels_count}")

