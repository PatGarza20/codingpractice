## Function to find the longest common prefix between all strings given.

def longestCommonPrefix(strs):
    # Get the shortest string in the array.
    short = min(string for string in strs)

    # Removes shortest string from array.
    strs.remove(short)

    # Starting from the full shortest string as the longest possible prefix,
    # works its way down to the first letter before declaring there is no common prefix.
    for iter in range(len(short), 0, -1):
        substring = short[:iter]
        val = 0

        for string in strs:
            # TryExcept to avoid a ValueError crash if substring is not found in string.
            try:
                if string.index(substring) == 0:
                    val += 1
            except:
                return "No common prefix found."

            if val == len(strs):
                return substring
    
    return "No common prefix found."


if __name__ == "__main__":
    strs = ["helloworld", "hellokitty", "hell"]
    # prints "hell"
    print(longestCommonPrefix(strs))

    strs = ["daily", "interview", "pro"]
    # prints 'No common prefix found.'
    print(longestCommonPrefix(strs))