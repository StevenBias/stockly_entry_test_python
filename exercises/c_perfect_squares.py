"""
# Exercice: Perfect Squares

## Explanation:
You must code a function that given a lower bound and upper bound returns an array containing all
the perfect squares (see Further Notice) between the lower bound and the upper bound included.
The array must be sorted from lower to upper.

## Example:
```
perfect_squares(3, 15) == [4, 9]
```

## Expected Time
You should spend around 10 minutes on this exercice

## Further Notice
- You have more examples in <root>/tests/test_c_perfect_squares.py
- An integer n is said to be a perfect squares if there exists an integer i such that `i * i = n`
For example 4 = 2 * 2 is a perfect squares but 5 isn't.
"""


def perfect_squares(lower, upper):
    # Write your code here
    lst = []
    for i in range(upper + 1):
        if i*i > upper*upper:
            return lst
        if i*i >= lower and i*i <= upper:
            lst.append(i*i)
    return lst
