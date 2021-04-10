# Number To Words
The module numberToWords.py converts an integer to it's English representation in words. For example, if the integer 56 is entered, the function will return
Fifty Six. The function supports 3 features.

* FEATURE_NUMBERS_GREATER_THAN_99
    * Supports numbers greater than 99
* FEATURE_NEGATIVE_NUMBERS
    * Supports negative numbers
* FEATURE_INCLUDE_THE_WORD_AND
    * Include 'And' for a number preceded by a multiple of 100

## Steps
1. Deals with special values (e.g. 0)
2. Deals with negative integers
3. Deals with out of range values
4. Loop through billions, millions, thousands, and hundreds. Decrement the integer moving from left to right (e.g. 432 -> 32)
5. Determine the remainder below 100
6. Returns integer in words