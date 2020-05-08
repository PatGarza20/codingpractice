## Function to check if one string is an anagram of the other.

def isAnagram(string, anagram):
    string = list(string)
    anagram = list(anagram)

    # If their lengths are unequal, we already know string is not an anagram.
    if len(string) != len(anagram):
        return "not an anagram"

    # Sets cannot hold duplicate values, making them ideal to check if both
    # strings use the same set of letters.
    setString = sorted(set(string))
    setAnagram = sorted(set(anagram))

    if setString != setAnagram:
        return("not an anagram") 
    else:
        # Using the sets as keys, creates dictionaries to count how many times
        # each letter appears in string/anagram. e.g [a : 0, b : 0, ...]
        dictString = dict(zip(setString, [0]*len(setString)))
        dictAnagram = dict(zip(setAnagram, [0]*len(setAnagram)))

        for iter in range(len(string)):
            dictString[string[iter]] += 1
            dictAnagram[anagram[iter]] += 1

        if dictString == dictAnagram:
            return "is an anagram"
        else:
            return "is not an anagram"

if __name__ == "__main__":
    print(isAnagram("baguette", "etgabuet"))