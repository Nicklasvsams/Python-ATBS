from difflib import Match
import re

# () = groups
# [] = define char class - Allows you to define your own char class ie [a-zA-Z] matches all letters from a-z lower and uppercase
# {n, m} = match pattern/group n amount of times up to m times - Succeeds the pattern/group you want to match n amount of times, 
#                                                                you leave out either n or m to have no lower/upper bound ie {3,} or {,3},
#                                                                use only a single digit to max a specific amount of times ie {3}
#                                                                use a questionmark (?) after braces to match the shortest string possible ie {3,5}?
# \ = escape character - Precedes any special character you want to acutally check for ie. \(
# ? = optional matching - Succeeds the match you want to be optional
# | = either/or matching - Will alway choose the first occurence of either of the options
# * = match pattern/group zero or more times - Succeeds the pattern/group you want to match zero or more times
# + = match pattern/group one or more times - Suceeds the pattern/group you want to match one or more times
# ^ = must start with - Precedes the first pattern and defines that the string must start with this pattern
# $ = must end with - Succeeds the last pattern and defines that the string must end with this pattern
# . = wildcard character = Will match any char that isn't a newline
# \d = any char which is digit 0-9
# \D = any char not a digit 0-9
# \w = any letter, numeric digit or underscore char
# \W = any char that is not a letter, numeric digit or underscore char
# \s = any space, tab or newline char
# \S = any char that isn't space, tab or newline
# re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE) = multiple optional parameters
# IGNORECASE = ignores lower and uppercase
# DOTALL = includes all characters, even newline
# VERBOSE = enables you to spread out your regex string for better readability (remember triple quotations marks ''')


# Can be done with regex: \d{3}-\d{3}-\d{4}
def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
             return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')

# Find phone number in string
phoneNumRegex = re.compile(r'(\(?\d{3}\)?)?-?(\d{3}-\d{4})')

mo = phoneNumRegex.findall('My landline number is (415)-555-4242, my mobile number is 415-666-2143, this is my number for my contact person: 334-3367')

for i in range(len(mo)):
    print('Regex found phone number: Area code: ' + mo[i][0] + ' Main number: ' + mo[i][1])