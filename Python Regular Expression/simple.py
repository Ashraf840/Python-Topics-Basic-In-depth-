import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Has HasHas

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800@555@1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

# print(r"\tTab")  # Regular expression will interpret the string before Python doing anything
# Create pattern, case-sensitive; follows alphabet order strictly
# pattern = re.compile(r'.')  # Allows to separate the patterns into variables; reuse the variables to multiple searches

# Scenario: Match email
# pattern = re.compile(r'coreyms.com')    # [ Works OK ]
# pattern = re.compile(r'coreyms\.com')   # escape the backslash-dot

# Scenario: Pattern to find any (single) digit from 0-9
# pattern = re.compile(r'\d')

# Scenario: Pattern to find anything which is not a digit from 0-9; includes special characters, whitespaces, tabs, newlines
# pattern = re.compile(r'\D')

# Scenario: Pattern to find a word character (a-z, A-Z, 0-9); ignore the special characters
# pattern = re.compile(r'\w')

# Scenario: Pattern to find any whitespace, tab, newline
# pattern = re.compile(r'\s')

# Scenario: Pattern to find not whitespace, tab, newline. 
# Includes alphabets with the special characters . ^ $ * + ? { } [ ] \ | ( )
# pattern = re.compile(r'\S')

# # Scenario: Pattern to find the "Has" which has word-boundaries after
# pattern = re.compile(r'Has\b')

# Scenario: Pattern to find the "Has" which doesn't have word-boundaries after
# pattern = re.compile(r'Has\B')

# Use the pattern that matches literal characters into the string
# matches = pattern.finditer(text_to_search)

sentence = 'Start a sentence and then bring it to an end'

# # Caret (^) matches the beginning of the string
# pattern = re.compile(r'^Start')
# matches = pattern.finditer(sentence)

# # Dollar ($) matches the end of the string
# pattern = re.compile(r'an$')
# matches = pattern.finditer(sentence)



# # Scenario: Pattern to find the phone nums within the multiline string.
# # To match the first 3 digits of the phone nums use the "\d\d\d".
# # To match the dot(.) or hyphen(-) in between, use dot(.) in the pattern.
# # To match the middle 3 digits, again use the "\d\d\d". Use dot(.) to match whether the dot/hyphen.
# # Then the last 4 digits will be matched using "\d\d\d\d".
# pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d') # matches any char in the phone-numbers

# Use character-set (brackets) to define which chars to be considered
pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d') # matches only the dot(.) or hypen(-) chars in the phone-numbers

# Use the pattern that matches literal characters into the string
matches = pattern.finditer(text_to_search)



count = 0

for match in matches:
    print(match)
    count += 1
    # print(match.span())
    # print(text_to_search[match.span()[0]:match.span()[1]])

print("Total matches: ", count)