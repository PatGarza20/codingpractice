## You are the manager of a number of employees who all sit in a row. The CEO would like to give bonuses to all of your employees, but since the company did not perform so well this year the CEO would like to keep the bonuses to a minimum.

## The rules of giving bonuses is that:
## - Each employee begins with a bonus factor of 1x.
## - For each employee, if they perform better than the person sitting next to them, the employee is given +1 higher bonus (and up to +2 if they perform better than both people to their sides).

## Given a list of employee's performance, find the bonuses each employee should get.

def getBonuses(nums):
    bonuses = [1]*len(nums)

    # edge cases
    if len(nums) <= 1:
        return bonuses

    if nums[0] > nums[1]:
        bonuses[0] += 1
    
    if nums[-1] > nums[-2]:
        bonuses[-1] += 1

    for iter in range(1, len(nums) - 1):
        # performed better than both sides
        if nums[iter - 1] < nums[iter] and nums[iter + 1] < nums[iter]:
            bonuses[iter] += 2
        
        # performed better than one side
        elif nums[iter - 1] < nums[iter] or nums[iter + 1] < nums[iter]:
            bonuses[iter] += 1

    return bonuses

if __name__ == "__main__":
    # prints [1,2,3,1,2,3,1]
    print(getBonuses([1, 2, 3, 2, 3, 5, 1]))