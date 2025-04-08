# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 :
            return 1
        len_trust = len(trust)
        trust_dict = defaultdict(list)
        trust_dict2 = defaultdict(int)
        

        for i in range(len(trust)):
            trust_dict[trust[i][0]].append( trust[i][1])
            trust_dict2[trust[i][1]] += 1

        ans = -1 
        for i in range(len(trust)):
            if trust_dict2[trust[i][1]] == n - 1 and len(trust_dict[trust[i][1]]) == 0:
                return trust[i][1]
        return -1


        