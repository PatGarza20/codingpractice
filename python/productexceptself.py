## Given an array of integers, this function returns an array in which each element
## is the product of every element in the array except the number at that index.
## e.g [1,2,3,4,5] -> [120,60,40,30,24] since the first number is 2 x 3 x 4 x 5, second is 1 x 3 x 4 x 5, etc.

def products(nums):
    results = []

    for iter in range(len(nums)):
        num = 1
        for iterTwo in range(len(nums)):
            if iterTwo != iter:
                num *= nums[iterTwo]

        results.append(num)

    return results

if __name__ == "__main__":
    # prints [120, 60, 40, 30, 24]
    print(products([1,2,3,4,5]))