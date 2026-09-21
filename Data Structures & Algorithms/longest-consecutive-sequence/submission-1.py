class Solution:
    def find(self, v):
        if self.p[v] == v:
            return v
        self.p[v] = self.find(self.p[v])
        return self.p[v]
    
    def unite(self, u, v):
        u = self.find(u)
        v = self.find(v)

        if u == v:
            return False
        
        if self.s[u] > self.s[v]:
            self.p[v] = u
            self.s[u] += self.s[v]
        else:
            self.p[u] = v
            self.s[v] += self.s[u]
        return True

    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        self.p = dict()
        self.s = dict()

        for i in set(nums):
            self.p[i] = i
            self.s[i] = 1

        answer = 1
        for i in self.p:
            if (i - 1) in self.p:
                self.unite(i - 1, i)
        
        for i in self.p:
            answer = max(answer, self.s[self.find(i)])

        return answer

        