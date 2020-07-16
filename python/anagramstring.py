## This function takes a string and anagram, then returns every index in string where the anagram is found.
## e.g ('acdbacdacb', 'abc') returns [3, 7] since an anagram of 'abc' is found starting at indexes 3 and 7.

def findAnagrams(string, anagram):
    start = 0
    end = len(anagram)
    indexes = []
    
    while end <= len(string):
        sub = string[start:end]
        
        # Using sets, you can simply verify that the substring and anagram contain the same letters.
        if set(sub) == set(anagram):
            indexes.append(start)

        start += 1
        end += 1

    return indexes

if __name__ == "__main__":
    # prints [3, 7]
    print(findAnagrams('acdbacdacb', 'abc'))