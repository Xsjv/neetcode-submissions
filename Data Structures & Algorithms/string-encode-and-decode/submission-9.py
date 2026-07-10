class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "IAMEMPTYSECRET"
        encoding = "%_%".join(strs)
        encoding += "%_%"
        return encoding
    def decode(self, s: str) -> List[str]:
        if s == "IAMEMPTYSECRET":
            return []
        r = []
        a = 0
        b = 0
        for i, char in enumerate(s):
            if s[i:(i + 3)] == "%_%":
                r.append(s[a:b])
                a = b + 3
                b += 1
            else:
                b += 1
        return r
