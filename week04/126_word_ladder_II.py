class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        letters = [chr(ord("a") + i) for i in range(26)]

        end = collections.defaultdict(list) # map of (end word: list of word sequence)
        end[beginWord] = [[beginWord]]
        available = set(wordList)
        while end:
            temp = collections.defaultdict(list)
            for w in end:
                if w == endWord:
                    return end[w]

                for i in range(len(w)):
                    for c in letters:
                        w2 = w[:i] + c + w[i + 1:]
                        if w2 != w and w2 in available:
                            temp[w2] += [l + [w2] for l in end[w]]
            available -= set(temp.keys())
            end = temp
        return []