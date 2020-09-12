## Given an array of unsorted numbers, verify whether a single number can be
## changed to make the array "non-decreasing".
## i.e array[i] <= array[i + 1] holds for every i (1 <= i < n)

# If more than one instance where array[i] > array[i + 1]
# is found, we know to return False.
def nonDecreasing(nums):
    count = 0
    
    for iter in range(len(nums) - 1):
        if nums[iter] > nums[iter + 1]:
            count += 1

        if count > 1:
            return False
    
    return True


if __name__ == "__main__":
    nums = [13, 4, 7]
    # prints True
    print(nonDecreasing(nums))

    nums = [5, 1, 3, 2, 5]
    # prints False
    print(nonDecreasing(nums))