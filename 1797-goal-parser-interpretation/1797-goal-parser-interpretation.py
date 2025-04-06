class Solution:
    def interpret(self, command: str) -> str:
        n = len(command)
        ans = []
        i = 0
        while i<n:
            if command[i]=='G':
                ans.append('G')
                i += 1
            elif command[i:i+2]=='()':
                ans.append('o')
                i += 2
            elif command[i:i+4]=='(al)':
                ans.append('al')
                i += 4
        return "".join(ans)