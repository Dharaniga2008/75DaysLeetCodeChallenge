class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_string = ""
        curr_num = 0

        for ch in s:

            # If digit, build the number
            if ch.isdigit():
                curr_num = curr_num * 10 + int(ch)

            # If opening bracket
            elif ch == '[':
                stack.append((curr_string, curr_num))

                # Reset for new substring
                curr_string = ""
                curr_num = 0

            # If closing bracket
            elif ch == ']':
                prev_string, num = stack.pop()

                # Repeat current string
                curr_string = prev_string + num * curr_string

            # Normal character
            else:
                curr_string += ch

        return curr_string