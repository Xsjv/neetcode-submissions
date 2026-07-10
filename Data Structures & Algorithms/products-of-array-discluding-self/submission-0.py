class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        fp = 1
        zeroCount = 0
        for x in nums:
            if x == 0:
                zeroCount += 1
            else:
                fp *= x
        if zeroCount >= 2:
            return [0] * len(nums)
        finalList = []
        if zeroCount == 1:
            for x in nums:
                if x != 0:
                    finalList.append(0)
                else:
                    finalList.append(fp)
            return finalList
        for x in nums:
            finalList.append(fp // x)

        return finalList