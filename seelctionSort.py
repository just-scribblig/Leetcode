class Solution: 
    def selectionSort(self, arr):
        #code here
        n = len(arr)
        sorted = []
        for i in range(n-1):
            temp = i
            for j in range(i+1, n):
                if arr[j] < arr[temp]:
                    temp = j
            arr[temp], arr[i] = arr[i], arr[temp]
        return arr
