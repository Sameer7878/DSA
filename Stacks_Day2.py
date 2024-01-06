class Stacks:

    def isValid(self, s: str) -> bool:
        """
        using pre-defined hashMap to parentheses list and stack
        iterate the string if the closed parentheses check its open parentheses to validate order
        :param s:
        :return:
        """
        closeToOpen = {')': '(', '}': '{', ']': '['}
        stack = [ ]
        for i in s:
            if i in closeToOpen:
                if stack and stack.pop() == closeToOpen [ i ]:
                    continue
                else:
                    return False
            stack.append(i)
        return not stack

    def evalRPN(self, tokens: list [ str ]) -> int:
        """
        using stack
        iterate the string if any arthematic operator string found it calculate arthematic operation using two number which are pushed into stack
        :param tokens:
        :return:
        """
        stack = [ ]
        for i in tokens:
            if i == '*':
                stack.append(stack.pop() * stack.pop())
            elif i == '+':
                stack.append(stack.pop()+stack.pop())
            elif i == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif i == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(i))
        return stack [ 0 ]

    def generateParenthesis(self, n: int) -> list [ str ]:
        """
        using stack

        :param n:
        :return:
        """
        # conditions
        # add open paratheses if opened<n
        # return result if opened==closed==n
        # add close paratheses if closed<opened
        stack = [ ]
        res = [ ]

        def backTrack(openN, closeN):
            """

            :param openN:
            :param closeN:
            :return:
            """
            if openN == closeN == n:
                res.append(''.join(stack))
                return
            if openN < n:
                stack.append('(')
                backTrack(openN+1, closeN)
                stack.pop()
            if closeN < openN:
                stack.append(')')
                backTrack(openN, closeN+1)
                stack.pop()

        backTrack(0, 0)
        return res

    def dailyTemperatures(self, temperatures: list [ int ]) -> list [ int ]:
        """
        using stack to store the pair of temperature value and its index.
        checks linear values if condition matches update the result in corresponding indexes
        :param temperatures:
        :return:
        """
        stack = [ ]
        res = [ 0 ] * len(temperatures)
        for n, t in enumerate(temperatures):
            while stack and t > stack [ -1 ] [ 0 ]:
                stackT, stackInd = stack.pop()
                res [ stackInd ] = n-stackInd
            stack.append([ t, n ])
        return res

    def carFleet(self, target: int, position: list [ int ], speed: list [ int ]) -> int:
        """

        :param target:
        :param position:
        :param speed:
        :return:
        """
        stack = [ ]
        carPairs = [ [ p, s ] for p, s in zip(position, speed) ]
        for i in sorted(carPairs) [ ::-1 ]:
            stack.append((target-i [ 0 ]) / i [ 1 ])
            if len(stack) >= 2 and stack [ -2 ] >= stack [ -1 ]:
                stack.pop()
        return len(stack)

    def largestRectangleArea(self, heights: list [ int ]) -> int:
        """
        using stack to store the pair of index and heights of histogram
        pop the histogram from the stack if height of the histogram is smaller than the previous ones
        and update the maxArea
        :param heights:
        :return:
        """
        maxArea = 0
        stack = [ ]
        for i, n in enumerate(heights):
            start = i
            while stack and stack [ -1 ] [ 1 ] > n:
                prevInd, h = stack.pop()
                maxArea = max(maxArea, (i-prevInd) * h)
                start = prevInd
            stack.append([ start, n ])
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights)-i))
        return maxArea


class MinStack:

    def __init__(self):
        self.stack = [ ]
        self.minStack = [ ]

    def push(self, val: int) -> None:
        """

        :param val:
        :return:
        """
        self.stack.append(val)
        val = min(val, self.minStack [ -1 ] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        """

        :return:
        """
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        """

        :return:
        """
        return self.stack [ -1 ]

    def getMin(self) -> int:
        """

        :return:
        """
        return self.minStack [ -1 ]
