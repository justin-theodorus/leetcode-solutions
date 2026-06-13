class MinStack:

    def __init__(self):
        self.stack = []
        self.min_arr = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_arr or val < self.min_arr[-1]:
            self.min_arr.append(val)
        else:
            self.min_arr.append(self.min_arr[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.min_arr.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_arr[-1]
        
"""
minStack.push(1);
minStack.push(2);
minStack.push(0);
minStack.getMin(); // return 0
minStack.pop();
minStack.top();    // return 2
minStack.getMin(); // return 1

[1,2,0]

find the min after every push? 
[1,1,0]
"""
