import collections
class SlidingWindow:
    def maxProfit(self, prices: list [ int ]) -> int:
        """
        Input: prices = [7,1,5,3,6,4]
        Output: 5
        Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
        Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

        :param prices:
        :return:
        """
        profit = 0
        l, r = 0, 1
        while r < len(prices) and l < len(prices):
            if prices [ r ] > prices [ l ]:
                profit = max(profit, prices [ r ]-prices [ l ])
            else:
                l = r
            r += 1

        return profit

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Input: s = "abcabcbb"
        Output: 3
        Explanation: The answer is "abc", with the length of 3.

        :param s:
        :return:
        """
        maxS = 0
        charSet = set()
        l = 0
        for r in range(len(s)):
            while s [ r ] in charSet:
                charSet.remove(s [ l ])
                l += 1
            charSet.add(s [ r ])
            maxS = max(maxS, r-l+1)
        return maxS
    '''def excutionTime(self,n,logs):
        res={}
        liveTask=''
        resumedStack=[]
        for log in logs:
            taskNo,taskState,taskStartNo=log.split(':')
            if taskState=='start':
                if liveTask:
                    res[liveTask]=res
                liveTask=taskNo
                res[taskNo]=1
            elif taskState:
                liveTask=resumedStack.pop()
                res[]'''

    def characterReplacement(self, s: str, k: int) -> int:
        """
        Input: s = "ABAB", k = 2
        Output: 4
        Explanation: Replace the two 'A's with two 'B's or vice versa.

        :param s:
        :param k:
        :return:
        """
        maxS = 0
        count = {}
        l = 0
        for r in range(len(s)):
            count [ s [ r ] ] = 1+count.get(s [ r ], 0)
            while (r-l+1)-max(count.values()) > k:
                count [ s [ l ] ] -= 1
                l += 1
            maxS = max(maxS, r-l+1)
        return maxS

    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Input: s1 = "ab", s2 = "eidbaooo"
        Output: true
        Explanation: s2 contains one permutation of s1 ("ba").
        -> here we need to check the permutations of string s1 is matches to substring of s2
        ->I use two hashmaps for two strings to store the frequency of characters od strings
        -> check every window of s2 if it matches return True else False
        :param s1:
        :param s2:
        :return:
        """
        if len(s1) > len(s2):
            return False
        s1m = {}
        s2m = {}
        for i in range(len(s1)):
            s1m [ s1 [ i ] ] = 1+s1m.get(s1 [ i ], 0)
            s2m [ s2 [ i ] ] = 1+s2m.get(s2 [ i ], 0)
        l = 0
        for r in range(len(s1), len(s2)):
            if all([ x in s2m and s2m [ x ] == y for x, y in s1m.items() ]):
                return True
            s2m [ s2 [ r ] ] = 1+s2m.get(s2 [ r ], 0)
            s2m [ s2 [ l ] ] -= 1
            l += 1
        return all([ x in s2m and s2m [ x ] == y for x, y in s1m.items() ])

    def minWindow(self, s: str, t: str) -> str:
        """
        Input: s = "ADOBECODEBANC", t = "ABC"
        Output: "BANC"
        Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

        -> Here I use two for two strings (s and t). the hashmaps contain characters of strings with frequency
        -> used two check points have and need variables need is count of characters of T and iterating string s and update have variable when matches string T characters
        -> if have==need update the result if its length less than old one and shrink the window by updating left pointer

        :param s:
        :param t:
        :return:
        """
        if t == "":
            return ""
        countT = {}
        window = {}
        for i in t:
            countT [ i ] = 1+countT.get(i, 0)
        have = 0
        need = len(countT)
        l = 0
        res = ''
        for r in range(len(s)):
            window [ s [ r ] ] = 1+window.get(s [ r ], 0)
            if s [ r ] in countT and countT [ s [ r ] ] == window [ s [ r ] ]:
                have += 1
            while have == need:
                if len(res) > r-l+1 or res == '':
                    res = s [ l:r+1 ]
                window [ s [ l ] ] -= 1
                if s [ l ] in countT and window [ s [ l ] ] < countT [ s [ l ] ]:
                    have -= 1
                l += 1
        return res


    def maxSlidingWindow(self, nums: list [ int ], k: int) -> list [ int ]:
        """
        using que data structure for decreasing array and stack for increasing array
        ->Before appending the number into queue , check if topmost number is greater than the appending number
        if it is nums[r]>q[-1] then pop the element and append this new number else append new number.

        -> if len of window is greater and equal to k then update and result array and left pointer
        Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
        Output: [3,3,5,5,6,7]
        Explanation:
        Window position                Max
        ---------------               -----
        [1  3  -1] -3  5  3  6  7       3
         1 [3  -1  -3] 5  3  6  7       3
         1  3 [-1  -3  5] 3  6  7       5
         1  3  -1 [-3  5  3] 6  7       5
         1  3  -1  -3 [5  3  6] 7       6
         1  3  -1  -3  5 [3  6  7]      7

        :param nums:
        :param k:
        :return:
        """
        res = [ ]
        q = collections.deque()
        l, r = 0, 0
        while r < len(nums):

            while q and nums [ q [ -1 ] ] < nums [ r ]:
                q.pop()
            q.append(r)

            if l > q [ 0 ]:
                q.popleft()

            if r+1 >= k:
                res.append(nums [ q [ 0 ] ])
                l += 1
            r += 1
        return res