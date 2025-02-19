from collections import deque


# Using 2 queues (assume the deque used here is just a queue not a double ended one)
# Time: O(1) for Push, O(1) for Top, O(1) for Empty, O(N) for Pop
# Space: O(N)
class MyStack:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        if self.queue1:
            self.queue1.append(x)
        else:
            self.queue2.append(x)

    def pop(self) -> int:
        if self.queue1:
            while self.queue1:
                if len(self.queue1) == 1:
                    return self.queue1.pop()
                self.queue2.append(self.queue1[0])
                self.queue1.popleft()
        else:
            while self.queue2:
                if len(self.queue2) == 1:
                    return self.queue2.pop()
                self.queue1.append(self.queue2[0])
                self.queue2.popleft()

    def top(self) -> int:  # Assuming that slicing isn't allowed
        if self.queue1:
            while self.queue1:
                if len(self.queue1) == 1:
                    top = self.queue1.pop()
                    self.queue2.append(top)
                    return top
                self.queue2.append(self.queue1[0])
                self.queue1.popleft()
        else:
            while self.queue2:
                if len(self.queue2) == 1:
                    top = self.queue2.pop()
                    self.queue1.append(top)
                    return top
                self.queue1.append(self.queue2[0])
                self.queue2.popleft()

    def empty(self) -> bool:
        return True if not self.queue1 and not self.queue2 else False


# Using a single queue
# Time: O(1) for all except O(N) for pop
# Space: O(N)
class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        for i in range(len(self.q) - 1):
            self.push(self.q.popleft())
        return self.q.popleft()

    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return len(self.q) == 0


# Queue Of Queues
# Time: O(1) for all
# Space: O(N)
class MyStack:

    def __init__(self):
        self.q = None

    def push(self, x: int) -> None:
        self.q = deque([x, self.q])

    def pop(self) -> int:
        top = self.q.popleft()
        self.q = self.q.popleft()
        return top

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return not self.q


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
