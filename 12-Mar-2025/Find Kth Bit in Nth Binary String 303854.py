# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        iters = math.ceil(math.log(k+1,2))
        temp = ['0']
        for i in range(iters-1):
            temp.append('1')
            reversed_part = temp[-2::-1] 
            inverted_part = ['1' if x == '0' else '0' for x in reversed_part]  
            temp.extend(inverted_part)  
           
        return temp[k-1]
         
        