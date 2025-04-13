class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = list("".join(char.lower()) for char in s if char.isalnum())
        d = deque(s)
        n = len(d)
        while len(d)>1:
            if d.popleft() != d.pop():
                return False
        return True