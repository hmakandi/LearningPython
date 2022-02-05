###Hacker Rank Code!!!!##############
#!/bin/python3

import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
    
###Initiate variables i to iterate matrix, and s_word to store list
i=0
s_word=[]
###Regex for matching during replace. Compile in advance makes better use of resources for regex expressions
p = re.compile(r'(?<=\w)([\$\#\%\s]+)(?=\w)')

###Go through the matrix given, and put each character in a list s_word
while i<m:
    [s_word.append(x[i]) for x in matrix]
    i+=1
#Make the list into a sentence and store in variable word
word=''.join(s_word)   

##Apply previously compiled regex p to be substitured by space 
print(p.sub(" ",word))
