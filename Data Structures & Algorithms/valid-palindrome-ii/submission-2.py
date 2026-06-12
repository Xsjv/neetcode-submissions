class Solution:
    def validPalindrome(self, s: str) -> bool:
        pal_ready = ''
        for char in s:
            if char.isalnum():
                pal_ready += char.lower()
        for x in range(len(pal_ready)):
            skip = False
            temp_pal = pal_ready[:x] + pal_ready[x+1:]
            a = 0
            b = len(temp_pal) - 1
            if x == len(pal_ready):
                b += 1
                while a < b:
                    if pal_ready[a] != pal_ready[b]:
                        skip = True
                        break
                    a += 1
                    b -= 1
            else:
                while a < b:
                    if temp_pal[a] != temp_pal[b]:
                        skip = True
                        break
                    a += 1
                    b -= 1
            if skip == True:
                continue
            return True
        return False
            