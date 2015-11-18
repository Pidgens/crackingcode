__author__ = 'derekchiu'

# Implement an algorithm to determine if a string has all unique characters. What
# if you cannot use additional data structures?
def uniqueChars(string):
    # ASCII is 256, Unicode is 1000000+
    seen = [False] * 256
    for dchar in string:
        ascii_val = ord(dchar)
        if seen[ascii_val] is True:
            return False
        seen[ascii_val] = True
    return True

# If two strings are anagrams
def anagram(string1, string2):
    if len(string1) != len(string2):
        return False
    total_letters = [False] * 256
    for i in string1:
        total_letters[ord(i)] = True
    for j in string2:
        if total_letters[ord(j)] == False:
            return False
    return True