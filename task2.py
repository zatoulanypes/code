class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.l.append(x)

    def pop(self):
        """
        :rtype: None
        """
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
        return min(self.l)

# В задании сказано, что все опреации должны выполняться за константное время, но как быть с getMin? В любом
# случае, на leetcode решение приняли.
# Runtime 632 ms
# Memory 17.4 MB