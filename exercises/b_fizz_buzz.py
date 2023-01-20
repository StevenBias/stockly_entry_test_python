"""
# Exercice: Fizz Buzz

## Explanation:
You must code a function that given an integer n will output an array of length n such that:
 - On indexes multiple of 3 it contains 'fizz'
 - On indexes multiple of 5 it contains 'buzz'
 - On indexes multiple of 3 and 5 it contains 'fizzbuzz'
 - On every other index it contains ''

## Example:
```
fizz_buzz(6) == ['fizzbuzz', '', '', 'fizz', '', 'buzz']
```

## Expected Time
You should spend around 5 minutes on this exercice

## Further Notice
You have more examples in <root>/tests/test_b_fizz_buzz.py
"""

def my_fizz_buzz(n):
    # Write your code here
    if n%3 == 0 and n%5 == 0:
        return "fizzbuzz"
    elif n%3 == 0:
        return "fizz"
    elif n%5 == 0:
        return "buzz"
    else:
        return ""

def fizz_buzz(n):
    lst = []
    for i in range(n):
       lst.append(my_fizz_buzz(i))

    return lst
