## Function that takes an array of tuples and returns it without overlapping intervals.
## e.g [(1, 3), (5, 8), (4, 10), (20, 25)] => [(1, 3), (4, 10), (20, 25)]
## because (5,8) is included in the interval (4,10).

def merge(tuples):
    # A copy is made to avoid altering the original array of tuples.
    tuplesCopy = tuples.copy()

    for iter in range(len(tuples)):
        for iterTwo in range(len(tuples)):
            if tuples[iter][0] > tuples[iterTwo][0] and tuples[iter][1] < tuples[iterTwo][1]:
                # Sets the overlapped values to 0 in tuplesCopy to indicate it's overlapped.
                tuplesCopy[iter] = 0
                break

    # Removes all overlapped values.
    tuplesCopy = list(x for x in tuplesCopy if x != 0)

    return tuplesCopy

if __name__ == "__main__":
    tuples = [(1, 3), (5, 8), (4, 10), (20, 25)]

    # prints [(1, 3), (4, 10), (20, 25)]
    print(merge(tuples))