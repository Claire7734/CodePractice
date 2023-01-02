class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i in range(len(s)):
            last[s[i]] = i
        anchor = -1
        ans = []
        cur = 0
        for i in range(len(s)):
            cur = max(cur, last[s[i]])
            if cur == i:
                ans.append(cur - anchor)
                anchor = cur
        return ans