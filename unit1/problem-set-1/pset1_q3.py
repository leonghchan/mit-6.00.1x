"""
Pset 1 - Problem 3

Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in 
alphabetical order. For example if s = 'azcbobobegghakl', then your program should print:
Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example if s = 'abcbcd', then your program
should print:
Longest substring in alphabetical order is: abc
"""

# iterate over each character in string, s.
# two cases: s[i+1] >= s[i] or not.
# first case: then add s[i+1] to substring.
# second case: either substring is greater than or less than the longest substring.
# re-define substring starting from most recent character.

s = "azcbobobegghakl"
sub = s[0]
longest_sub = ""
for i in range(len(s) - 1):
    if s[i + 1] >= s[i]:
        sub += s[i + 1]
    else:
        if len(sub) > len(longest_sub):
            longest_sub = sub
        sub = s[i + 1]

if len(sub) > len(longest_sub):
    longest_sub = sub

print("Longest substring in alphabetical order is: ", longest_sub)

