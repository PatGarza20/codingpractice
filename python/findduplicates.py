## Function to find which values in an array have duplicates.
## This function uses a set -> dictionary trick to emphasize speed, ease of use, and readability.

def findDuplicates(data):
    results = []

    # Creating a sorted set from data removes all duplicate values in data.
    # The set is then zipped into a dictionary so that counting the quantity of values in data is simple and fast.
    # e.g [1,3,1,2,3,2,1] --> [1,2,3] --> {1: 0, 2: 0, 3: 0}
    setData = sorted(set(data))
    dictData = dict(zip(setData, [0]*len(setData)))

    for iter in range(len(data)):
        item = data[iter]
        dictData[item] += 1

        if dictData[item] > 1:
            results.append(item)

    return results

if __name__ == "__main__":
    data = [4,3,2,7,8,2,3,1]

    print(findDuplicates(data))