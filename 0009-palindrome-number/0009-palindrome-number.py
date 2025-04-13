class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        if s[0] == ['-']:
            return False
        d = deque(s)
        while len(d)>1:
            if d.popleft() != d.pop():
                return False
        return True