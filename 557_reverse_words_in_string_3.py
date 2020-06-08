'''
557. Reverse Words in a String III

Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.

'''


class Solution:
    def reverseWords(self, s):
        '''
        splitting the string into an array
        looping through the array and replacing the words with the reverse of the word
        joining the array back into a string, separated with spaces
        '''
        s = s.split()
        for i, word in enumerate(s):
            s[i] = word[::-1]
        return " ".join(s)

        '''
        one-liner
        '''
        # return " ".join([i[::-1] for i in s.split()])


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.reverseWords("the sky is blue"))
