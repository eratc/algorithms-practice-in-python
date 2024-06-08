import math


def create_sparse_table(arr):
    n = len(arr)
    m = math.ceil(math.log2(n))
    sparse_table = [[] for i in range(m)]
    sparse_table[0] = [ele for ele in arr]
    for i in range(1, m):
        for j in range(n):
            if j + 2**i > n:
                break
            sparse_table[i].append(min(sparse_table[i-1][j], sparse_table[i-1][j+2**(i-1)]))
    for row in sparse_table:
        print(row)
    return sparse_table


def rmq(sparse_table, left, right):
    dist = math.floor(math.log2(right - left + 1))
    return min(sparse_table[dist][left], sparse_table[dist][right - 2**dist + 1])


def main():
    arr = [9, 4, 12, 5, 1, 7, 9, 11, 3, 6, 4, 7]
    sparse_table = create_sparse_table(arr)
    for i in range(9):
        print(rmq(sparse_table, i, i+3))


if __name__ == '__main__':
    main()
