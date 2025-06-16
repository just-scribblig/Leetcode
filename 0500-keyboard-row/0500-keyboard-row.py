class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'}
        row2 = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'}
        row3 = {'z', 'x', 'c', 'v', 'b', 'n', 'm'}

        result = []
        
        for i in words:
            if all(j.lower() in row1 for j in i):
                result.append(i)
            elif all(j.lower() in row2 for j in i):
                result.append(i)
            elif all(j.lower() in row3 for j in i):
                result.append(i)

        return result