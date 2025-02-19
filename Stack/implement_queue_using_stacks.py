# Using two stacks
# Time: O(1) for push & empty and O(n) for pop and peek
# Space: O(n)
class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        for _ in range(len(self.stack1) - 1):
            self.stack2.append(self.stack1.pop())
        top = self.stack1.pop()
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return top

    def peek(self) -> int:
        for _ in range(len(self.stack1) - 1):
            self.stack2.append(self.stack1.pop())
        top = self.stack1.pop()
        self.stack2.append(top)
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return top

    def empty(self) -> bool:
        return not self.stack1


# Using Two Stacks (Amortized Complexity) i.e. we are saving time by appointing pushing
# to stack1 and popping to stack2 always
# Time: O(1) for push and empty and O(1) amortized time for pop and peek
class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self) -> bool:
        return True if not self.stack1 and not self.stack2 else False
