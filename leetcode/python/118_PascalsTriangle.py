class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(1, numRows):
            pre = ans[i-1]
            cur = [0]*(i+1) # Create space!!!
            for j in range(i + 1):
                if j == 0:
                    cur[j] = 1
                elif j == i:
                    cur[j] = 1
                    ans.append(cur)
                else:
                    cur[j] = pre[j] + pre[j-1]
        return ans
