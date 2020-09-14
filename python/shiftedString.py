## Function which determines if string A can be shifted some number of times to get string B.

def isShifted(a, b):
    if a == b:
        return True

    a = list(a)
    b = list(b)

    for iter in range(len(b)):
        temp = a.pop(0)
        a.append(temp)

        if a == b:
            return True

    return False

if __name__ == "__main__":
    a = "abcde"
    b = "cdeab"

    # prints True
    print(isShifted(a, b))