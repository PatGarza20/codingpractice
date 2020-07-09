## A criminal is constructing a ransom note - given a stack of cut-out letters, this function
## determines whether they have the necessary letters to construct the word they want.

def canSpell(letters, note):
    # Uses set -> dict to give us a count of how many letters we have.
    setLetters = sorted(set(letters))
    dictLetters = dict(zip(setLetters, [0]*len(setLetters)))

    for letter in letters:
        dictLetters[letter] += 1

    # Converts note to a list w/o spaces.
    note = list(note.replace(" ",""))

    # If letter in note isn't in our pile, immediately fails.
    # If dictLetters[letter] goes below zero, fails since there is no more of that letter.
    for letter in note:
        if letter not in dictLetters:
            return False
        else:
            dictLetters[letter] -= 1

            if dictLetters[letter] < 0:
                return False

    return True

if __name__ == "__main__":
    # prints "True"
    print(canSpell(['a','b','c','d','e','f'], "bed"))

    # prints "False"
    print(canSpell(['a','b','c','d','e','f'], "cat"))