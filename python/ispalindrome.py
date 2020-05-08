## Function to check if a string is a palindrome.

def isPalindrome(string):
    string = list(string)

    for iter in range(len(string)):
        if string[iter] != string[-iter - 1]:
            return "not a palindrome"
    return "is a palindrome"

if __name__ == "__main__":
    print(isPalindrome("racecar"))