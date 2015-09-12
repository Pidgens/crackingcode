def uniqueChars(string):
	# parse of the string, use an array to store every character, compare the character
	strArray = list(string)
	checkList = []
	for item in strArray:
		if item in checkList and item is not " ":
			return False
		else:
			checkList.append(item)
	return True

def unique(string):
	charSet = [None] * 256
	for i in range(0, len(string)):
		value = ord(string[i])
		if charSet[value] and string[i] is not ' ':
			return False
		charSet[value] = True
	return True

print("Question 1 \n")
print(unique('         '))
print(unique('dude'))
print(unique('kid champ l'))

def revcStyle(string):
	return None

def removeDup(string):
	if len(string) < 2:
		return string
	if string == None:
		return
	bufferIndex = 1
	stringArray = list(string)
	for i in range(0, len(stringArray)):

		for j in range(0, bufferIndex):
			if stringArray[i] == stringArray[j]:
				break
		if j == bufferIndex:
			stringArray[bufferIndex] = stringArray[i]
			bufferIndex+=1
		stringArray[bufferIndex] = ''
	return ''.join(stringArray)

print("\nQuestion 3\n")
print(removeDup("follow up"))

def ifAnagram(string1, string2):
    if len(string1) != len(string2):
        return False
    strArray = [0] * 256
    uniquenumChars = 0
    completedChars = 0
    str_one = list(string1)
    for c_item in str_one:
        print 'C_ITEM:%s' % c_item
        if strArray[ord(c_item)] == 0:
            ++uniquenumChars
        ++strArray[ord(c_item)]
    print strArray
    for str2_index in range(0, len(string2)):
        c = ord(string2[str2_index])
        print 'C: %s' % c
        if strArray[c]==0:
            return False
        --strArray[c]
        if strArray[c] == 0:
            ++completedChars
            print 'STR2_INDEX %s' % str2_index
            if completedChars == uniquenumChars:
                return str2_index == len(string2)-1
    return False


print("\nQuestion 4 \n")
#print(ifAnagram("dog", "god"))
print(ifAnagram("kid", "kid"))


def replaceSpace(string):
	index = -1
	charArray = list(string)
	for item in charArray:
		index += 1
		if item is " ":
			charArray[index] = "%20"
	return ''.join(charArray)

print("\nQuestion 5")
print(replaceSpace('dog hey'))
print(replaceSpace('              ok ' ))