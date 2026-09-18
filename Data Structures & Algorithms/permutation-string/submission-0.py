class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s1 -> counter(s1)
        # s2 -> moving window of length s1
        if len(s1) > len(s2):
            return False

        counter1 = [0 for i in range(26)]
        counter2 = [0 for i in range(26)]

        for i in range(len(s1)):
            counter1[ord(s1[i]) - ord('a')] += 1
            counter2[ord(s2[i]) - ord('a')] += 1
        
        l = 0
        for r in range(len(s1), len(s2)):
            if counter1 == counter2:
                return True
            
            counter2[ord(s2[l]) - ord('a')] -= 1
            counter2[ord(s2[r]) - ord('a')] += 1
            l += 1
        
        return counter1 == counter2