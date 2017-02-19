from collections import defaultdict


class Solution(object):

    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        max_length = 0
        levels = defaultdict(int)
        node_len, level, isfile = 0, 0, False
        for c in input:
            if c == '\n':
                levels[level] = node_len + ((levels[level - 1] + 1) if level > 0 else 0)
                if isfile:
                    max_length = max(levels[level], max_length)
                node_len, level, isfile = 0, 0, False
            elif c == '\t':
                level += 1
            else:
                if c == '.':
                    isfile = True
                node_len += 1
        levels[level] = node_len + ((levels[level - 1] + 1) if level > 0 else 0)
        if isfile:
            max_length = max(levels[level], max_length)
        return max_length



s = Solution()
print s.lengthLongestPath("a")
print s.lengthLongestPath("dir\n\t        file.txt\n\tfile2.txt")
print s.lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")
