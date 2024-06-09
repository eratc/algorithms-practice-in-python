class DSU:
    def __init__(self):
        self.parent = {}
        self.size = {}

    def add_set(self, val):
        self.parent[val] = val
        self.size[val] = 1

    def find_set(self, val):
        root = val
        while self.parent[root] != root:
            root = self.parent[root]
        return root

    def union_sets(self, val1, val2):
        set1 = self.find_set(val1)
        set2 = self.find_set(val2)
        if set1 != set2:
            if self.size[set1] < self.size[set2]:
                set1, set2 = set2, set1
            self.parent[set2] = set1
            self.size[set1] += self.size[set2]

    def print_set(self, val):
        result = []
        root = self.find_set(val)
        for node, parent in self.parent.items():
            if self.find_set(parent) == root:
                result.append(node)
        print(f"Set {root}: {result}")


def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    dsu = DSU()
    for ele in arr:
        dsu.add_set(ele)
    dsu.union_sets(1, 2)
    dsu.union_sets(3, 4)
    dsu.union_sets(5, 6)
    dsu.union_sets(7, 8)
    dsu.union_sets(5, 8)
    for ele in arr:
        print(f"{ele} belongs to:")
        dsu.print_set(ele)


if __name__ == '__main__':
    main()
