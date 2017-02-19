

class Solution(object):


    def parse_tokens(self, s):
        number = ''
        for c in s:
            if c == ' ':
                continue
            elif c in ('+', '-', '*', '/'):
                yield int(number)
                yield c
                number = ''
            else:
                number += c
        if number:
            yield int(number)

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.calculate_op(self.calculate_op(self.parse_tokens(s), ('*', '/')), ('+', '-')).next()

    def calculate_op(self, tokens, ops):
        left = tokens.next()
        op = next(tokens, None)
        while op is not None:

            right = tokens.next()
            if op in ops:
                left = self.do_op(op, left, right)
            else:
                yield left
                yield op
                left = right
            op = next(tokens, None)
        yield left

    def do_op(self, op, left, right):
        if op == '*':
            return left * right
        elif op == '/':
            return left / right
        elif op == '+':
            return left + right
        elif op == '-':
            return left - right

s = Solution()

print s.calculate("3+2*2"), 7
print s.calculate("3/2"), 1
print s.calculate("3+5 / 2 "), 5
