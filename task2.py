class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l = []
        self.mins = [None]
        self.current_min = None

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.l.append(x)
        if self.current_min is None or x <= self.current_min:
            self.current_min = x
            self.mins.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if self.l[-1] == self.current_min:
            self.mins.pop()
            self.current_min = self.mins[-1]
        self.l.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.l[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.current_min

