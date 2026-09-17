class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()
        for i in strs:
            content = [0 for _ in range(26)]
            for j in i:
                content[ord(j) - ord('a')] += 1
            
            key = tuple(content)
            if key in anagrams:
                anagrams[key].append(i)
            else:
                anagrams[key] = [i]
        
        return list(anagrams.values())