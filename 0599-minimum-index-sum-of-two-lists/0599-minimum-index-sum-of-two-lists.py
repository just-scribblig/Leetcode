class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res = defaultdict(int)
        n1 = len(list1)
        n2 = len(list2)

        for i in range(n1):
            for j in range(n2):
                if list1[i] == list2[j]:
                    res[list1[i]] = i + j
        
        minimum = math.inf
        ans = []
        for (k,v) in res.items():
            if v<minimum:
                minimum = v
                ans = [k]
            elif v==minimum:
                ans.append(k)
        
        return ans