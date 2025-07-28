# Problem: Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def isValid(part: str) -> bool:
           
            if not part:
                return False
            if len(part) > 1 and part[0] == '0':
                return False
            if int(part) > 255:
                return False
            return True

        def backtrack(start: int, path: List[str]):
           
            if len(path) == 4:
                if start == len(s):
                    answer.append(".".join(path))
                return
            
          
            for end in range(start + 1, min(start + 4, len(s) + 1)):
                part = s[start:end]
                if isValid(part):
                    backtrack(end, path + [part])

        answer = []
        backtrack(0, [])
        return answer
