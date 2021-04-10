'''
This module converts an integer to it's English representation in words. For example, if the integer 56 is entered, the function will return
Fifty Six. The function supports 3 features.

FEATURE_NUMBERS_GREATER_THAN_99 (supports numbers greater than 99)
FEATURE_NEGATIVE_NUMBERS (supports negative numbers)
FEATURE_INCLUDE_THE_WORD_AND (Include 'And' for a number preceded by a multiple of 100)

1. Deals with special values (e.g. 0)
2. Deals with negative integers
3. Deals with out of range values
4. Loop through billions, millions, thousands, and hundreds. Decrement the integer moving from left to right (e.g. 432 -> 32)
5. Determine the remainder below 100
6. Returns integer in words
'''

# import ld client for launchDarkly
import ldclient
from ldclient.config import Config

# setting key for launchDarkly
ldclient.set_config(Config(sdk_key = "sdk-e1cd70a1-f68f-4b96-8461-8214c479ccea"))
ld_client = ldclient.get()

# user model for launchDarkly dashboard
user = {
    "key": "kyle.reynolds9146@gmail.com",
    "firstName": "Kyle",
    "lastName": "Reynolds",
    "email": "kyle.reynolds9146@gmail.com",
    "custom": {
      "groups": ["Google", "Microsoft"]
    }
}

# Feature Flags
FEATURE_NUMBERS_GREATER_THAN_99 = ld_client.variation("numbers-greater-than-99", {"key": "kyle.reynolds9146@gmail.com"}, False)
FEATURE_NEGATIVE_NUMBERS = ld_client.variation("negative-numbers", {"key": "kyle.reynolds9146@gmail.com"}, False)
FEATURE_INCLUDE_THE_WORD_AND = ld_client.variation("include-the-word-and", {"key": "kyle.reynolds9146@gmail.com"}, False)

# Define MAXIMUM_INTEGER and Multiples
# application code to show the feature
if FEATURE_NUMBERS_GREATER_THAN_99:
    MAXIMUM_INTEGER = 999999999999999 # 999 trillion
    Multiples = (
        (1000000000000, ' Trillion '),
        (1000000000, ' Billion '),
        (1000000, ' Million '),
        (1000, ' Thousand '),
        (100, ' Hundred '))
# the code to run if the feature is off
else:
    MAXIMUM_INTEGER = 99

# Dictionary of the word (value) corresponding to each integer (key).
IntegerWords = {
    1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine',
    10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Ninteen',
    20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety'}

def integerToWords(integer):
    '''
    Turns an integer into it's English words.
    '''
    # 1. Deals with special values (e.g. 0)
    if integer == 0:
        return 'Zero'

    # Initialize the return value 'words'
    words = ''

    # 2. Deals with negative integers
    if integer < 0:
        if FEATURE_NEGATIVE_NUMBERS:
            words = 'Negative '
            integer *= -1 # make integer positive
        else:
            return 'Unknown'

    # 3. Deals with out of range values
    if MAXIMUM_INTEGER < integer:
        return 'Unknown'

    # 4. Loop through billions, millions, thousands, and hundreds. Decrement the integer moving from left to right (e.g. 4321 -> 321)
    if FEATURE_NUMBERS_GREATER_THAN_99:
        for multiple, word in Multiples:
            if multiple <= integer:
                digits = integer // multiple # The floor of 4321 // 1000 = 4.
                integer -= digits * multiple # Get rid of the 4000 (e.g. 4321 -> 321)
                words += integerToWords(digits) + word # 'Four' + ' Thousand ' + 'Three' + ' Hundred ' 
                if FEATURE_INCLUDE_THE_WORD_AND:
                    # Include 'And' for a number preceded by a multiple of 100.
                    # For instance 321 => 'Three Hundred and Twenty One'
                    if multiple == 100 and integer != 0:
                        words += 'and '

    # 5. Determine the remainder below 100
    if integer != 0:
        if integer in IntegerWords:
            # integer is directly in IntegerToWords
            words += IntegerWords[integer]
        else:
            # integer is 21, 32, 98, etc
            words += IntegerWords[10 * (integer // 10)] + ' ' + IntegerWords[integer % 10]

    # 6. Returns integer in words
    return words.strip()

#####################################################################################################################################
# Testing
for integer in (-999999, -909, -1, 0, 1, 21, 101, 432, 1001, 123456, 123456789012345, 1234567890123456):
    print(str(integer) + ': ' + integerToWords(integer))
# print(integerToWords(99))

# close out launchDarkly client
ld_client.close()