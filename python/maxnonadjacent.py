## Function to find the largest possible sum given that no elements are adjacent to eachother.
## e.g [2,1,2,7,3], largest non-adjacent sum is 2 (index 0) + 7 (index 3) = 9.

def maxNonAdjacent(nums):
    largest = 0

    for iter in range(len(nums)):
        for iterTwo in range(iter + 2, len(nums)):
            sum = nums[iter] + nums[iterTwo]

            if sum > largest:
                largest = sum

    return largest

if __name__ == "__main__":
    # prints 5 (4 + 1)
    print(maxNonAdjacent([3,4,1,1]))

    # prints 9 (2 + 7)
    print(maxNonAdjacent([2,1,2,7,3]))