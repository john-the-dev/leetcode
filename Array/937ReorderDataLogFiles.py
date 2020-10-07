# 937. Reorder Data in Log Files
'''
You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

Return the final order of the logs.

 

Example 1:

Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
 

Constraints:

0 <= logs.length <= 100
3 <= logs[i].length <= 100
logs[i] is guaranteed to have an identifier, and a word after the identifier.
'''
from common import *
class Solution:
    '''
    Sort based on 2 keys.
    O(MNlog(N)) runtime, O(MN) storage, in which M is maximum size of a single log and N is the size of logs.
    Beat 98% runtime, 11% storage of all Leetcode submissions.
    '''
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []
        for i,log in enumerate(logs):
            k = log.find(' ')
            if log[k+1].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append([log[k+1:],log[:k]])
        letter_logs.sort()
        out = []
        for log,id in letter_logs:
            out.append('{} {}'.format(id,log))
        for log in digit_logs:
            out.append(log)
        return out

assert(Solution().reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]) == ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"])
assert(Solution().reorderLogFiles(["dig1 8 1 5 1"]) == ["dig1 8 1 5 1"])
assert(Solution().reorderLogFiles([]) == [])
assert(Solution().reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]) == ["a2 act car","g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"])  # Test when letter logs tie we need to use id to sort.