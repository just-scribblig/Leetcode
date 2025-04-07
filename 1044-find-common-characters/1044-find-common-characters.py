class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        n = len(words)
        ans = Counter(words[0])
        for i in range(n):
            ans = ans & Counter(words[i])
        return list(ans.elements())