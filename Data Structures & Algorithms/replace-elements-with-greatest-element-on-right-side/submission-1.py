class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        N = len(arr)
        greatest = -1
        ans = [0] * N
        for i in range(N - 1, -1, -1):
            ans[i] = greatest
            greatest = max(arr[i], greatest)
        return ans