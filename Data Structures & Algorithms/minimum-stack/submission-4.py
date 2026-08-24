class MinStack:

    def __init__(self):
        self.s = []
        self.smin = []

    def push(self, val: int) -> None:
        self.s.append(val)
        val = min(val, self.smin[-1] if self.smin else val)
        self.smin.append(val)
        

    def pop(self) -> None:
        self.s.pop()
        self.smin.pop()
        

    def top(self) -> int:
        return self.s[-1]
        

    def getMin(self) -> int:
        return self.smin[-1]
        
