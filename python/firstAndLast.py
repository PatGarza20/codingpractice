## This function finds the first and last occurrences of a target element in linear time.

def getRange(arr, target):
    front = -1
    end = -1

    # Using front/end == -1 as a condition ensures they are only set once.
    for iter in range(len(arr)):
        if arr[iter] == target and front == -1:
            front = iter

        if arr[-iter] == target and end == -1:
            end = len(arr) - iter
    
    return "[{} , {}]".format(front, end)

if __name__ == "__main__":
    arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
    target = 2

    # Prints [1, 4]
    print(getRange(arr, target))