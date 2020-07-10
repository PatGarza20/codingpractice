## This function rotates a list k amount of times without generating a new array.
## e.g [1,2,3,4,5], k = 2 --> [3,4,5,1,2] 

def rotateList(nums, k):
    # pop(0) deletes the first object in nums 
    while k > 0:
        temp = nums.pop(0)
        nums.append(temp)

        k -= 1

    return nums

if __name__ == "__main__":
    nums = [1,2,3,4,5]
    print(rotateList(nums, 2))