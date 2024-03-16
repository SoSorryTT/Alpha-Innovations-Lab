def solve(wordList, target):
    word_dict = {}
    for i in range(len(wordList)):
        if wordList[i] in word_dict:
             return (wordList[i], wordList[i])
        word_dict[wordList[i]] = i

    for i in range(1, len(target)):
        prefix = target[:i]
        suffix = target[i:]

        if prefix in word_dict and suffix in word_dict and word_dict[prefix] != word_dict[suffix]:
                return (wordList[word_dict[prefix]], wordList[word_dict[suffix]])
    
    return None 


# Test cases
wordList1 = ["ab", "bc", "cd"]
target1 = "abcd"
print(solve(wordList1, target1))

wordList2 = ["ab", "bc", "cd"]
target2 = "cdab"
print(solve(wordList2, target2))

wordList3 = ["ab", "bc", "cd"]
target3 = "abab"
print(solve(wordList3, target3))

wordList4 = ["ab", "ba", "ab"]
target4 = "abab"
print(solve(wordList4, target4)) 