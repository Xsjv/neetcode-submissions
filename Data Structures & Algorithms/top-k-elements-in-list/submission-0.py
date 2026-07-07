class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = {}
        r = (-1,-1) # first number, second frequency
        f = []
        for x in nums:
            if x in s:
                s[x] += 1
            else:
                s[x] = 1
        for _ in range(k):
            for x in s:
                if s[x] > r[1]:
                    r = (x, s[x])
            f.append(r[0])
            s.pop(r[0])
            r = (-1, -1)
        return f
        
