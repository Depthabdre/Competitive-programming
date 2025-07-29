# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]  # Base frame for score

        for char in s:
            if char == '(':
                stack.append(0)  # Start a new score frame
            else:
                last = stack.pop()  # Pop the last score inside parentheses
                if last == 0:
                    stack[-1] += 1  # Base case: "()"
                else:
                    stack[-1] += 2 * last  # Nested case: "(A)" → 2*A

        return stack[0]
