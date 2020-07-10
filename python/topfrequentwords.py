## Given a list of words, returns the k most frequent words.
## The words are sorted from highest to lowest frequency.

def topFrequent(words, k):
    # set -> dict is used to obtain the frequency of each word
    result = []
    setWords = sorted(set(words))
    dictWords = dict(zip(setWords, [0]*len(setWords)))

    for word in words:
        dictWords[word] += 1
   
    # This loop sorts the dictionary by value, the reverse flag
    # gives us the highest -> lowest order we need.
    for word in sorted(dictWords, key=dictWords.get, reverse=True):
        # print(word, dictWords[word])
        result.append(word)

        k -= 1
        if k == 0:
            break

    return result

if __name__ == "__main__":
    words = ["daily", "interview", "pro", "pro", "for", "daily", "pro", "problems"]
    k = 5

    # prints ['pro', 'daily', 'for', 'interview', 'problems']
    print(topFrequent(words, k))