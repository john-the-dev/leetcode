# 68. Text Justification
'''
Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
Example 1:

Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified becase it contains only one word.
Example 3:

Input:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
'''
from common import *
class Solution:
  '''
  Rule: scan through the words, identify the words for a given line with maxWidth constraint, then allocate spaces accordingly.
  O(n*maxWdith) runtime, O(k) storage, in which n is # of lines in output and k is the max # of words within 1 line.
  Beat 56% runtime, 100% storage of all Leetcode submissions.
  '''
  def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
      i,n,out = 0,len(words),[]
      while i < n:
        j,total,padding,formats = i,0,0,[]
        while j < n and total+padding+len(words[j]) <= maxWidth:
          total += padding+len(words[j])
          formats.append([j,padding])
          j += 1
          padding = 1
        padding,k,right_padding = maxWidth-total,j-i,0
        if k > 1 and j < n:
          extra_padding = padding // (k-1)
          extra = padding % (k-1)
          for m in range(1,k):
            if extra > 0:
              formats[m][1] += extra_padding+1
              extra -= 1
            else:
              formats[m][1] += extra_padding
        else:
          right_padding = padding
        temp = []
        for m in range(k):
          temp.append(' '*formats[m][1])
          temp.append(words[formats[m][0]])
        if right_padding > 0: temp.append(' '*right_padding)
        out.append(''.join(temp))
        i = j
      return out

# Tests.
assert(Solution().fullJustify(["What","must","be","acknowledgment","shall","be"], 16) == ["What   must   be","acknowledgment  ","shall be        "])
assert(Solution().fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20) == ["Science  is  what we","understand      well","enough to explain to","a  computer.  Art is","everything  else  we","do                  "])

          
          
          

          

