## This function uses a nested loop to find all words in a list that are
## a concatenation of two words in the array. e.g "techlead" = "tech" + "lead"

def findAllConcatenatedWords(words):
    result = []
    concats = set()

    # loop to form set of all possible concatenations of two words
    for word in words:
        # If word is already in list of concatenations, 
        # we know to skip the loop.
        if word in concats:
            continue
        
        for iter in range(len(words)):
            concatOne = word + words[iter]
            concatTwo = words[iter] + word

            concats.add(concatOne)
            concats.add(concatTwo)
    
    # loop to find results
    for word in words: 
        if word in concats:
            result.append(word)
        
    return result

if __name__ == "__main__":
    words = ["techlead", "tech", "lead", "cat", "cats", "dog", "catsdog"]

    # prints "['techlead', 'catsdog']"
    print(findAllConcatenatedWords(words))