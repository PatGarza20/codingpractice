## There are n people lined up with heights represented as integers.
## If a murder happens in front of them, only people taller than everyone in front of them witness it.
## This function finds the witnesses.
## i.e witnesses [3, 6, 3, 4, 1] => [murder scene]

def findWitnesses(witnesses):
    canSee = []
    tallest = 0

    # Loops backwards through witnesses.
    # If witness at iter is taller than tallest, they can see.
    for iter in range(len(witnesses) - 1, -1, -1):
        if witnesses[iter] > tallest:
            canSee.append(witnesses[iter])
            tallest = witnesses[iter]

    canSee.reverse()
    return canSee
        
if __name__ == "__main__":
    print(findWitnesses([3,6,3,4,1]))