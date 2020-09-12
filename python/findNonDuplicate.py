## Given a list of numbers in which every number appears twice except one,
## find that one number.

# This function uses a dictionary to count how many of each digit
# appear in nums. Then min() is used to find the least value
# in the dict and get the number we're looking for.
def singleNumber(nums): 
    numDict = {}

    for num in nums:
        if num not in numDict:
            numDict[num] = 1

        else:
            numDict[num] += 1

    return numDict[min(numDict.values())]

if __name__ == "__main__":
    nums = [5, 4, 3, 2, 5, 4, 1, 3, 2]

    # prints 1
    print(singleNumber(nums))