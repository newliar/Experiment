class Dfs:
    m = 0
    ans = 0

    def __init__(self, node_relation, a):
        self.node_relation = node_relation
        self.a = a
        for i in range(3620):
            self.m = 0
            if self.a[i] != 1:
                self.ooo(i)
                self.ans = max(self.ans, self.m)
        print(self.ans)

    def ooo(self, s):
        self.a[s] = 1
        for i in range(3620):
            if self.a[i] != 1 and self.node_relation[s][i]:
                self.m += 1
                self.a[i] = 1
                self.ooo(i)
