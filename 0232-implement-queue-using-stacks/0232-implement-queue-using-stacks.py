class MyQueue:

    def __init__(self):
        self.in_stack = []    # for push
        self.out_stack = []   # for pop/peek

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        # Ensure out_stack has elements in correct order
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()

    def peek(self) -> int:
        # Same logic as pop, but don't remove
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()