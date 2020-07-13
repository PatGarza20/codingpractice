## This function generates all subsets of a list of unique numbers and includes the empty set.

def generateAllSubsets(nums):
    result = [nums[x: y + 1] for x in range(len(nums)) for y in range(x, len(nums))]

    # for x in range(len(nums)):
    #   for y in range(x, len(nums)):
    #       yield nums[x: y + 1]

    result.append(nums[0:0])
    
    return result

if __name__ == "__main__":
    # prints [[1], [1, 2], [1, 2, 3], [2], [2, 3], [3], []]
    print(generateAllSubsets([1,2,3]))