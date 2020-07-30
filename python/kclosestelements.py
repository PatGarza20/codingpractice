## Given a list of sorted numbers and two integers k and x, this function finds the k closest numbers to the pivot x.
## e.g [1, 3, 7, 8, 9], k = 3, x = 5 ==> [7, 3, 8] 

def closestNums(nums, k, x):
    # Converts nums to a set since we don't need duplicate numbers
    # and sets enable much faster searching than arrays.
    closest = []
    iter = 1
    nums = set(nums)

    while len(closest) < k:
        greater = x + iter
        less = x - iter

        if greater in nums:
            closest.append(greater)
            if len(closest) == k:
                break

        if less in nums:
            closest.append(less)
            if len(closest) == k:
                break
        iter += 1

    return closest

if __name__ == "__main__":
    nums = [1, 3, 7, 8, 9]
    k = 3
    x = 5

    # prints [7, 3, 8]
    print(closestNums(nums, k, x))