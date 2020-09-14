## Given a list of numbers and a target number k, return whether or not
## two numbers in the list add up to k. Done in a single pass of the list.

def twoSum(nums, k):
    for iter in range(len(nums)):
        # Gets current num.
        num = nums[iter]

        # .copy() is used so no changes are made to nums.
        # current num is removed from tempNums to avoid adding it to itself.
        tempNums = nums.copy()
        tempNums.pop(iter)

        # tempNums is turned into a set for constant lookups.
        tempNums = set(tempNums)

        if num > 0:
            subNum = k - num

            if subNum in tempNums:
                return True
        
        elif num < 0:
            subNum = k + abs(num)

            if subNum in tempNums:
                return True

    return False

if __name__ == "__main__":
    nums = [4,7,1,-3,2]
    k = 5

    # prints "True"
    print(twoSum(nums, k))