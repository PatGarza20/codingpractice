## Given a string, determine if any character can be removed to create a palindrome.

# Method to check if a string (presented as a list) is a palindrome.
def checkPalindrome(word):
    x = len(word) - 1

    for iter in range(len(word)):
        if word[iter] != word[x - iter]:
            return False
    return True

# "temp = word.copy()" is used instead of "temp = word"
# because temp would be a direct reference to word otherwise and alter word's contents.
def createPalindrome(word):
    word = list(word)
    temp = word.copy()

    for iter in range(len(word)):
        temp.pop(iter)
        # If a palindrome is created by removing temp[iter], return True.
        if checkPalindrome(temp):
            return True
        temp = word.copy()

    return False

if __name__ == "__main__":
    print(createPalindrome("abcdcbea"))
    print(createPalindrome("abccba"))
    print(createPalindrome("abccaa"))