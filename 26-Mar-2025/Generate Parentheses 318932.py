# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        count = {"(":0, ")":0}
        path = []
        ans = []
        a = n * 2
        def bactrack(i):
            if i > a:
                ans.append("".join(path[:]))
                return
            if count['('] == count[')'] :
                path.append('(')
                count['('] += 1
                bactrack(i+1)
                path.pop()
                count['('] -= 1
               

            elif count['('] >= n:
                path.append(')')
                count[')'] += 1
                bactrack(i+1)
                path.pop()
                count[')'] -= 1
            else:
                path.append('(')
                count['('] += 1
                bactrack(i+1)
                path.pop()
                count['('] -= 1
                path.append(')')
                count[')'] += 1
                bactrack(i+1)
                path.pop()
                count[')'] -= 1
        bactrack(1)
        return ans