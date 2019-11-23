#!/usr/bin/env python

"""
==============================
BST 273 Homework #3, 30 points
==============================

NAME:
EMAIL:

Notes for completing BST 273 assignments:

* Fill in your name and school email address above.

* Do not share assignment code with other students.

* Lines containing questions to answer begin with "Q<X> (<Y>)",
  where <X> is the question number and <Y> is its point value.

* Questions will ask for a written response or a change/addition to Python
  code. Place written responses below the dashes ("----------") and above the
  closing set of triple quotes. Change/add code below the closing triple quotes.

* You do not need to (and shouldn't) change existing code in the assignment
  unless you are specifically requested to do so.

* Your submitted homework script must execute without errors.
"""

"""
Q1 (3). Complete the function <ci_match> ("case-insensitive match") to RETURN True
if the string argument <pattern> occurs as a substring of the string argument <text>
IGNORING DIFFERENCES IN CASE (e.g. treat "a" and "A" as the same character). HINT:
Converting <pattern> and <text> to be all lowercase before comparing them is one
way to enforce the case-insensitive comparison.
"""

def ci_match( pattern, text ):
    MATCH = False
    # your code here
    """
    1. change pattern to lowercase
    2. change text to lowercase
    3. use an if statement to check of formated_pattern is in formated_test
        if true change MATCH to True
    
    """
    formated_pattern = pattern.lower()
    formated_text = text.lower()
    if formated_pattern in formated_text:
        MATCH = True
    return MATCH

# testing code (leave unchanged in final submission)
print()
print("Q1: ci_match( 'FUN', 'function' ) returns True ->", ci_match('FUN', 'function'))
print( "Q1: ci_match( 'I', 'Team' ) returns False ->", ci_match("I", "Team"))
print()

"""
Q2 (5). Complete the function <list_add> to add the number passed as the argument <delta>
to each element of the list <numbers>. Your function should alter <numbers> IN PLACE and 
SHOULD NOT return a new list.
"""

def list_add( numbers, delta ):
    # your code here
    for i, number in enumerate(numbers):
        numbers[i] = number + delta
    return None

# testing code (leave unchanged in final submission)
test = [1, 2, 3]
print( "Q2: original list: [1, 2, 3] ->", test )
print( "Q2: list_add( <numbers>, 1 ) returns None ->", list_add(test, 1))
print( "Q2: modified list: [2, 3, 4] ->", test)
print( )

"""
Q3 (6). Complete the function <weird_sum> so that, given a list of numbers in <numbers>
as an argument, the function RETURNS (via the variable <ret>) the SUM of the numbers AFTER
each has been individually transformed according to the following rules:

1) If the number is negative, add its absolute value
2) If the number is even, add half its value
3) If the number is odd, add twice its value

More than one rule may apply to each number. If no rules apply to a number, you should 
still include it in your final sum.
"""

def weird_sum(numbers):
    ret = 0
    # your code here
    for num in numbers:
        #  If the number is negative, add its absolute value 
        num = abs(num)
        # If the number is even, add half its value
        if (num % 2) == 0: 
            num = (num // 2)
        # If the number is odd, add twice its value
        elif (num % 2) == 1: 
            num = (num * 2)
        ret += num
    return ret

# testing code (leave unchanged in final submission)
print( "Q3: weird_sum( [0.4, 0.6] ) returns 1.0 ->", weird_sum([0.4, 0.6]))
print( "Q3: weird_sum( [1, 2, 3] ) returns 9 ->", weird_sum([1, 2, 3]))
print( "Q3: weird_sum( [-1, 0.5, 2, 3] ) returns 9.5 ->", weird_sum([-1, 0.5, 2, 3]))
print()

"""
Q4 (6). Complete the function <count_vowels> to RETURN (as the variable <ret>) a DICT of
counts of the characters "AEIOU" in the string argument <text>. If the optional argument
<lower> is set to True, then also count "aeiou" as their uppercase equivalents.
"""

def count_vowels(text, lower=False):
    ret = {}
    # your code here
    for char in text:
        if not lower and char in  "AEIOU":
            if char in ret: ret[char] += 1
            else: ret[char] = 1
        elif lower and char in "AEIOUaeiou":
            letter = char.upper()
            if letter in ret: ret[letter] += 1
            else: ret[letter] = 1
    return ret

# testing code (leave unchanged in final submission)
print( "Q4: count_vowels( 'BANANA' ) returns {'A': 3} ->", count_vowels( "BANANA" ) )
print( "Q4: count_vowels( 'Area' ) returns {'A': 1} ->", count_vowels( "Area" ) )
print( "Q4: count_vowels( 'Area', lower=True ) returns {'A': 2, 'E': 1} ->", count_vowels( "Area", lower=True ) )
print( )
    
"""
Q5 (5). A prime number is an integer that only divides evenly into itself and 1. Complete
the <check_prime> function definition below to RETURN True if the integer argument <n>
is prime and False otherwise (via the returned variable <IS_PRIME>). You can accomplish
this by testing if <n> divides evenly into any of the numbers 2 though n-1 (and updating
<IS_PRIME> accordingly).
"""

def check_prime(n):
    IS_PRIME = True
    # your code here
    for i in range(n-1, 1, -1):
        if n % i == 0: 
            IS_PRIME = False
            break     
    return IS_PRIME

# testing code (leave unchanged in final submission)
print("Q5: check_prime( 23 ) returns True ->", check_prime(23))
print("Q5: check_prime( 24 ) returns False ->", check_prime(24))
print()

"""
Q6 (4). Using the <check_prime> function you made above, complete the <prime_range>
function to RETURN a LIST of the primes between 2 and <n> (the function's single integer
argument) via the returned variable <primes>. In Python style, do not include <n>
(the endpoint) in the list if it happens to be prime.
"""

def prime_range(n):
    primes = []
    # your code here
    for i in range(2, n):
        if check_prime(i): primes.append(i)
    return primes
    
# testing code (leave unchanged in final submission)
print( "Q6: prime_range( 10 ) returns [2, 3, 5, 7] ->", prime_range( 10 ) )
print( "Q6: prime_range( 13 ) returns [2, 3, 5, 7, 11] ->", prime_range( 13 ) )
print( )
    
"""
Q7 (1). Approximately how many hours did you spend on this assignment?
----------
<answers will vary>
"""