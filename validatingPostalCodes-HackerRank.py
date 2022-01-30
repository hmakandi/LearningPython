#Start ^ with digits 1-9,then other digits \d follow for the next 5 digits{5} and it ends $
regex_integer_in_range = r"^[1-9][\d]{5}$"	# Do not delete 'r'.
#For each digit \d skip forward ? to find the same digit \d after one step \1  
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"	# Do not delete 'r'.


import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
