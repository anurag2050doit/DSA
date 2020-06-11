"""
You are given a string S, and you have to find all the amazing substrings of S.

Amazing Substring is one that starts with a vowel (a, e, i, o, u, A, E, I, O, U).

Input

Only argument given is string S.
Output

Return a single integer X mod 10003, here X is number of Amazing Substrings in given string.
Constraints

1 <= length(S) <= 1e6
S can have special characters
Example

Input
    ABEC

Output
    6

Explanation
    Amazing substrings of given string are :
    1. A
    2. AB
    3. ABE
    4. ABEC
    5. E
    6. EC
    here number of substrings are 6 and 6 % 10003 = 6.

REF: https://www.interviewbit.com/problems/amazing-subarrays/

"""


class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        vowel = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        inc_counter = 0
        sum_counter = 0
        for l in A:
            if l in vowel:
                inc_counter += 1
            sum_counter = sum_counter + inc_counter
        return sum_counter % 10003


if __name__ == '__main__':
    obj = Solution()
    print(obj.solve('ABEC'))