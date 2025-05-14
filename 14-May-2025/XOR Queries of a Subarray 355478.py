# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefixXor = [0] * len(arr)
        run_xor = 0
        for i in range(len(arr)):
            run_xor ^= arr[i]
            prefixXor[i] = run_xor

        ans = []
        for L, R in queries:
            if L == 0:
                ans.append(prefixXor[R])
            else:
                ans.append(prefixXor[R] ^ prefixXor[L - 1])
        return ans
