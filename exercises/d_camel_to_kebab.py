"""
# Exercice: Camel To Kebab

## Explanation:
You must code a function that transforms a string from camelCase (see Further Notice) to
kebab-case (see Further Notice). This function must not break abreviations.

## Example:
```
camel_to_kebab('CamelCaseString') == 'camel-case-string'
camel_to_kebab('CamelCaseStringWithABREV') == 'camel-case-string-with-abrev'
camel_to_kebab('CamelCaseStringWithABREVInCenter') == 'camel-case-string-with-abrev-in-center'
```

## Expected Time
You should spend around 15 minutes on this exercice

## Further Notice
- You have more examples in <root>/tests/test_d_camel_to_kebab.py
- See [camelCase](https://en.wikipedia.org/wiki/Camel_case)
- See [kebabCase](http://wiki.c2.com/?KebabCase)
"""


def camel_to_kebab(str):
    # Lower first character
    s = str[0].lower()

    # Flag to detect a capital word
    capital_flag = False

    for i in range(1, len(str)):

        # Capital word detection
        capital_flag_old = capital_flag
        if i < (len(str) - 1):
            if str[i].isupper() and str[i+1].isupper():
                capital_flag = True
            else:
                capital_flag = False

        # Handle digits before
        # Handle digits after
        # Handle capital letter
        # Handle capital word
        if str[i].isnumeric()\
           or str[i-1].isnumeric()\
           or (str[i-1].islower() and str[i].isupper())\
           or capital_flag_old == True and capital_flag == False:
            s = s+'-'
            s = s+str[i].lower()
        else:
            s = s+str[i].lower()
    return s
