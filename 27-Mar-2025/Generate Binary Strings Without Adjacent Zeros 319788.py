# Problem: Generate Binary Strings Without Adjacent Zeros - https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/

class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []
        path = []

        def backtrack(i):
            if i == n:
                ans.append("".join(path[:]))
                return 
            
            if path and path[-1] == '0':
                path.append('1')
                backtrack(i+1)
                path.pop()
            else:
                path.append('1')
                backtrack(i+1)
                path.pop()
                path.append('0')
                backtrack(i+1)
                path.pop()
        backtrack(0)
        return ans
                
        