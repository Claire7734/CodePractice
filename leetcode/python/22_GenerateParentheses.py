class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.dfs(ans, [], 0, 0, n)
        return ans

    def dfs(self, ans, cur, left, right, n):
        if right == n:
            ans.append("".join(cur)) # Notice!!!
            return
        if left < n:
            cur += "("
            self.dfs(ans, cur, left+1, right, n)
            cur.pop()
        if right < left:
             cur += ")"
             self.dfs(ans, cur, left, right+1, n)
             cur.pop()