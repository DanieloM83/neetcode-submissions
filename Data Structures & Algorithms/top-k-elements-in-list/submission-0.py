class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = dict()
        maxn = 1

        for i in nums:
            counter[i] = counter.get(i, 0) + 1
            maxn = max(maxn, counter[i])
        
        freq = [[] for _ in range(maxn + 1)]
        for el, cnt in counter.items():
            freq[cnt].append(el)
        
        answer = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                answer.append(num)
                if len(answer) == k:
                    return answer

