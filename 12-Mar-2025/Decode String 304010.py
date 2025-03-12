# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        result = []

        for char in s:
            if stack and char != ']':
                if char.isdigit() and stack[-1].isdigit():
                    stack[-1] += char 
                else:
                    stack.append(char)
            elif not stack and char.isdigit():
                stack.append(char)
            elif not stack and char.isalpha():
                result.append(char)
            elif stack and char == ']':
                temp = ""
                while stack[-1] != '[':
                    temp = stack.pop() + temp  
                stack.pop()  
                
                temp *= int(stack.pop())  
                stack.append(temp)

                if len(stack) == 1:  
                    result.extend(stack)
                    stack = []

        return "".join(result)
