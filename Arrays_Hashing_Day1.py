"""
DAY: 1
CONCEPT: ARRAYS AND HASHING
DATE: 05/01/2024
"""
from collections import defaultdict, Counter


class ArraysHashing:

    def containsDuplicate(self, nums: list [ int ]) -> bool:
        """
        :param nums:
        :return: boolean

        timeComplexity: O(n)
        spaceComplexity: O(n)
        """
        hashSet = set()
        for n in nums:
            if n in hashSet:
                return True
            hashSet.add(n)
        return False

    def isAnagram(self, s: str, t: str) -> bool:
        """

        :param s:
        :param t:
        :return:
        """
        # return sorted(s)==sorted(t)
        # return Counter(s)==Counter(t)
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        for i in range(len(s)):
            countS [ s [ i ] ] = 1+countS.get(s [ i ], 0)
            countT [ t [ i ] ] = 1+countT.get(t [ i ], 0)
        for c in countS:
            if countS [ c ] != countT.get(c, 0):
                return False
        return True

    def twoSum(self, nums: list [ int ], target: int) -> list [ int ]:
        """

        :param nums:
        :param target:
        :return:
        """
        prevMap = {}  # val:index

        for i, n in enumerate(nums):
            diff = target-n
            if diff in prevMap:
                return [ prevMap [ diff ], i ]
            prevMap [ n ] = i

    def groupAnagrams(self, strs: list [ str ]) -> list [ list [ str ] ]:

        """
        :param strs:
        :return:
        """
        """
        GroupHashMap = defaultdict(list)
        for s in strs:
            GroupHashMap[''.join(sorted(s))].append(s)
        return GroupHashMap.values()
        """
        GroupHashMap = defaultdict(list)
        for word in strs:
            wordCount = [ 0 ] * 26
            for c in word:
                wordCount [ ord(c)-ord('a') ] += 1
            GroupHashMap [ tuple(wordCount) ].append(word)

        return GroupHashMap.values()

    def topKFrequent(self, nums: list [ int ], k: int) -> list [ int ]:
        """

        :param nums:
        :param k:
        :return:
        """
        countSorted = {k: v for k, v in sorted(Counter(nums).items(), key=lambda item: item [ 1 ], reverse=True)}
        return list(countSorted.keys()) [ :k ]

    def productExceptSelf(self, nums: list [ int ]) -> list [ int ]:
        """

        :param nums:
        :return:
        """
        res = [ 1 ] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res [ i ] = prefix
            prefix *= nums [ i ]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res [ i ] *= postfix
            postfix *= nums [ i ]
        return res

    def isValidSudoku(self, board: list [ list [ str ] ]) -> bool:
        """

        :param board:
        :return:
        """
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board [ r ] [ c ] == '.':
                    continue
                if (board [ r ] [ c ] in rows [ r ] or
                        board [ r ] [ c ] in cols [ c ] or
                        board [ r ] [ c ] in squares [ (r // 3, c // 3) ]):
                    return False
                cols [ c ].add(board [ r ] [ c ])
                rows [ r ].add(board [ r ] [ c ])
                squares [ (r // 3, c // 3) ].add(board [ r ] [ c ])
        return True

    def encode(self, strs: list [ str ]) -> str:
        """

        :param strs:
        :return:
        """
        encodeStr = ''
        for s in strs:
            encodeStr += str(len(s))+'#'+s
        return encodeStr

    def decode(self, s: str) -> list [ str ]:
        """

        :param s:
        :return:
        """
        res, i = [ ], 0
        while i < len(s):
            j = i
            while s [ j ] != '#':
                j += 1
            length = int(s [ i:j ])
            res.append(s [ j+1:j+1+length ])
            i = j+1+length
        return res

    def longestConsecutive(self, nums: list [ int ]) -> int:
        """

        :param nums:
        :return:
        """
        longest = 0
        numSet = set(nums)
        for n in nums:
            if (n-1) not in numSet:
                length = 0
                while (n+length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest
