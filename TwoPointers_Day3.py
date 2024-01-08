class TwoPointers:

    def isPalindrome(self, s: str) -> bool:
        """

        :param s:
        :return:
        """
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not self.alphaNumeric(s [ l ]):
                l += 1
            while l < r and not self.alphaNumeric(s [ r ]):
                r -= 1

            if s [ l ].lower() != s [ r ].lower():
                return False
            l += 1
            r -= 1
        return True

    def alphaNumeric(self, c):
        """

        :param c:
        :return:
        """
        return (ord('A') <= ord(c) <= ord('Z')) or (ord('a') <= ord(c) <= ord('z')) or (ord('0') <= ord(c) <= ord('9'))

    def twoSum(self, numbers: list [ int ], target: int) -> list [ int ]:
        """

        :param numbers:
        :param target:
        :return:
        """
        i, j = 0, len(numbers)-1

        while (i < j):
            twoSum = numbers [ i ]+numbers [ j ]
            if twoSum > target:
                j -= 1
            elif twoSum < target:
                i += 1
            else:
                return [ i+1, j+1 ]

    def threeSum(self, nums: list [ int ]) -> list [ list [ int ] ]:
        """

        :param nums:
        :return:
        """
        res = [ ]
        nums.sort()
        for i, n in enumerate(nums):
            if i > 0 and n == nums [ i-1 ]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                tSum = n+nums [ l ]+nums [ r ]

                if tSum > 0:
                    r -= 1
                elif tSum < 0:
                    l += 1
                else:
                    res.append([ n, nums [ l ], nums [ r ] ])
                    l += 1
                    while nums [ l ] == nums [ l-1 ] and l < r:
                        l += 1
        return res

    def maxArea(self, height: list [ int ]) -> int:
        """

        :param height:
        :return:
        """
        maxWater = 0
        i, j = 0, len(height)-1
        while i < j:
            area = (j-i) * min(height [ i ], height [ j ])
            maxWater = max(maxWater, area)

            if height [ i ] < height [ j ]:
                i += 1
            else:
                j -= 1
        return maxWater

    def trap(self, height: list [ int ]) -> int:
        """

        :param height:
        :return:
        """
        water = 0
        i, j = 0, len(height)-1
        leftMax = height [ 0 ]
        rightMax = height [ -1 ]
        while (i < j):
            if leftMax < rightMax:
                i += 1
                leftMax = max(leftMax, height [ i ])
                water += leftMax-height [ i ]
            else:
                j -= 1
                rightMax = max(rightMax, height [ j ])
                water += rightMax-height [ j ]
        return water