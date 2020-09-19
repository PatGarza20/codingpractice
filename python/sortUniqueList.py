## Given a list with only 3 unique numbers, sort the list in O(n) time.
## Focused on using hash maps (dict) and hash tables (set) to use constant space.

def sortNums(nums):
    # results in a sorted dict: [1: 0, 2: 0, 3: 0]
    setNums = set(nums)
    dictNums = dict(zip(setNums, [0]*len(setNums)))
    
    # fills dict with quantity of each num
    for num in nums:
        dictNums[num] += 1

    numList = []

    # creates a list for each num in dictNums, based on quantity of num
    # e.g numList = [[1, 1], [2, 2], [3, 3, 3]]
    for dictNum in dictNums:
        numList.append([dictNum] * dictNums[dictNum])

    final = numList[0] + numList[1] + numList[2]

    return final

if __name__ == "__main__":
    nums = [3, 3, 2, 1, 3, 2, 1]

    # prints [1, 1, 2, 2, 3, 3, 3]
    print(sortNums(nums))