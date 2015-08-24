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
	return null

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
	charArray1 = [0] * 256
	charArray2 = [0] * 256
	string1Array = list(string1)
	string2Array = list(string2)
	for i, element1 in enumerate(string1Array):
		if element1 is not ' ':
			charArray1[ord(element1)] += 1
	for element2 in string2Array:

		if element2 is not ' ':
			print ord(element2)
			print charArray2
			if charArray2[ord(element2)] > charArray1[ord(element2)]:
				return False
			charArray2[ord(element2)] += 1
	return True

print("\nQuestion 4 \n")
#print(ifAnagram("dog", "god"))
print(ifAnagram("kid", "kil"))


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