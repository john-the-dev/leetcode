# 721. Accounts Merge
'''
Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email that is common to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

Example 1:
Input: 
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
Explanation: 
The first and third John's are the same person as they have the common email "johnsmith@mail.com".
The second John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
Note:

The length of accounts will be in the range [1, 1000].
The length of accounts[i] will be in the range [1, 10].
The length of accounts[i][j] will be in the range [1, 30].
'''
from common import *
class Solution:
    '''
    Ad-hoc union find solution: use a hashmap to merge the groups.
    Beat 7% runtime, 6% storage of all Leetcode submissions.
    '''
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        groups,id,merge = {},0,{}
        for i,account in enumerate(accounts):
            s = set([id])
            for j in range(1,len(account)):
                if account[j] not in groups:
                    groups[account[j]] = [id,i]
                else:
                    s.add(groups[account[j]][0])
            
            while True:
                size = len(s)
                for item in merge:
                    if item in s: s.add(merge[item])
                    if merge[item] in s: s.add(item)
                if size == len(s): break
            v = min(s)
            for item in s:
                merge[item] = v
            id += 1
        emails = {}
        for email in groups:
            id,i = groups[email]
            id = merge[id]
            if id not in emails: emails[id] = ([accounts[i][0]],[])
            emails[id][1].append(email)
        out = []
        for id in emails:
            name_row,email_row = emails[id]
            email_row.sort()
            name_row.extend(email_row)
            out.append(name_row)
        return out

    '''
    Classic union find.
    Beat 62% runtime, 6% storage of all Leetcode submissions.
    '''
    def accountsMerge2(self, accounts: List[List[str]]) -> List[List[str]]:
        groups,emails = DSU(),{}
        for i,account in enumerate(accounts):
            for j in range(1,len(account)):
                if account[j] not in emails:
                    emails[account[j]] = i
                groups.union(emails[account[1]],emails[account[j]])
        ids = {}
        for email in emails:
            id = groups.find(emails[email])
            if id not in ids: ids[id] = {'name':[accounts[id][0]],'emails':[]}
            ids[id]['emails'].append(email)
        out = []
        for id in ids:
            ids[id]['emails'].sort()
            ids[id]['name'].extend(ids[id]['emails'])
            out.append(ids[id]['name'])
        return out

# Tests.
assert(Solution().accountsMerge([["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]) == [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]])
assert(Solution().accountsMerge([["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]) == [["David","David0@m.co","David1@m.co","David2@m.co","David3@m.co","David4@m.co","David5@m.co"]])
assert(Solution().accountsMerge2([["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]) == [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]])
assert(Solution().accountsMerge2([["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]) == [["David","David0@m.co","David1@m.co","David2@m.co","David3@m.co","David4@m.co","David5@m.co"]])
