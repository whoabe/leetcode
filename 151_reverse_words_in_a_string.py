'''
151. Reverse Words in a String

Given an input string, reverse the string word by word.



Example 1:

Input: "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.


Note:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.
'''


class Solution:
    '''
    approach 1
        1 liner easy
    '''
    # return " ".join(reversed(s.split()))

    '''
    approach 2
        if reversed isnt available to use, use [::-1]
    '''
    # return (" ".join(s.split()[::-1]))

    '''
    approach 3
        if reversed and [::-1] arent available for use
        First reverse entire string, then iterate over reversed string
        and again reverse order of characters within a word. Append each word to words.
    '''

    def reverseWords(self, s):
        word = ""
        words = ""
        s = s[::-1]
        for j, i in enumerate(s):
            # character is not space, a current word exists,
            # and previous character is space, e.g. i=b in " a b":
            if i != " " and word != "" and s[j-1] == " ":
                # add current word to words and append " " to later add this i
                words += (word + " ")
                word = i
            # character is not space, but it's either first character in string
            # or is part of current word, e.g. i=b in "b", " b" "ab", "a ab "
            elif i != " ":
                word = i + word
            else:
                continue

        words += word

        return(words)


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.reverseWords("the sky is blue"))
