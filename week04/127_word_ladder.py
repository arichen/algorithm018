from collections import defaultdict
class Solution:
    def __init__(self):
        self.wordMap = None

    def buildMap(self, wordList: List[str]):
        self.wordMap = defaultdict(list)
        for s in wordList:
            for k in self.mapKeys(s):
                self.wordMap[k].append(s)

    def mapKeys(self, s: str) -> List[str]:
        return [s[:i] + "*" + s[i + 1:] for i in range(len(s))]

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not endWord in wordList:
            return 0

        self.buildMap(set([beginWord] + wordList))

        queue = collections.deque([(beginWord, 1)])
        seen = set([beginWord])
        while queue:
            current, step = queue.popleft()
            if current == endWord:
                return step

            for k in self.mapKeys(current):
                words = self.wordMap[k]
                for w in words:
                    if not w in seen:
                        seen.add(w)
                        queue.append((w, step + 1))
        return 0