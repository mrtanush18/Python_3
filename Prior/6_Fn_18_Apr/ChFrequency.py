# Chk if removing atmost 1 character keeps count of each unique character same
# Ex. “xyyzz” : Yes, remove character ‘x’ to make frequency of each ch same.

M = 26

# Utility method to get index of character ch in lower alphabet characters
def getIdx(ch):
	return (ord(ch) - ord('a'))

# Returns true if all non-zero elements values are same
def allSame(freq, N):
	
	# get first non-zero element
	for i in range(0, N):
		if(freq[i] > 0):
			same = freq[i]
			break
		
	# check equality of each element with variable same	
	for j in range(i + 1, N):
		if(freq[j] > 0 and freq[j] != same):
			return False

	return True

# Returns true if we can make all character frequencies same
def possibleSameCharFreqByOneRemoval(str1):
	l = len(str1)

	# fill frequency array
	freq = [0] * M
	for i in range(0, l):
		freq[getIdx(str1[i])] += 1
		
	# if all frequencies are same,then return true
	if(allSame(freq, M)):
		return True
	
	# Try decreasing frequency of all character by one and then check all equality of all non-zero frequencies
	for i in range(0, 26):
		
		# Check character only if it occurs in str
		if(freq[i] > 0):
			freq[i] -= 1

			if(allSame(freq, M)):
				return True
			freq[i] += 1

	return False

# Driver code
if __name__ == "__main__":
	str1 = "xyyzz"
	if(possibleSameCharFreqByOneRemoval(str1)):
		print("Yes")
	else:
		print("No")

# o/p : Yes

'''
string1 = "xyyz" # size: 4 3 yes 121 [1,2]
string2 = "xyyzz" # size: 5 3 yes 122 [1,2]
string5 = "xxxxyyzz" # size: 8 3 no 422 [4,2]
string5 = "abbddffee" # size: 9 5 yes 12222 [1,2]
string5 = "aaabbddffee" # size: 11 5 yes 32222 [3,2]
'''