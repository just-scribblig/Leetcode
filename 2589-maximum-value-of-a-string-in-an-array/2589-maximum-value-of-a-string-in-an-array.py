class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        ans = -math.inf
        n = len(strs)
        for i in strs:
            if not i.isnumeric():
                ans = max(ans, len(i))
            else:
                ans = max(ans, int(i))
        return ans