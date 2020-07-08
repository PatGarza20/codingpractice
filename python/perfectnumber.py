## A "perfect number" is a positive integer that is equal to the sum of all its positive divisors except itself.
## e.g 28 = 1 + 2 + 4 + 7 + 14
## This function determines if a number is a perfect number.

def isPerfectNumber(num):
    total = 0

    for iter in range(1, num):
        if num%iter == 0:
            total += iter

    if total == num:
        return True
    return False

if __name__ == "__main__":
    # prints "True"
    print(isPerfectNumber(28))