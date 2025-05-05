# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class UnionFind:
    def __init__(self):
        self.parent = {}
        self.size = {}

    def find(self, x):
        if x != self.parent.setdefault(x, x):
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px != py:
            if self.size.get(px, 1) >= self.size.get(py, 1):
                self.parent[py] = px
                self.size[px] = self.size.get(px, 1) + self.size.get(py, 1)
            else:
                self.parent[px] = py
                self.size[py] = self.size.get(py, 1) + self.size.get(px, 1)
class Solution:
    def accountsMerge(self, accounts):
        uf = UnionFind()
        email_to_name = {}

        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                uf.union(first_email, email)
                email_to_name[email] = name

        root_to_emails = defaultdict(list)
        for email in email_to_name:
            root = uf.find(email)
            root_to_emails[root].append(email)

        result = []
        for root_email, group_emails in root_to_emails.items():
            name = email_to_name[root_email]
            result.append([name] + sorted(group_emails))

        return result
