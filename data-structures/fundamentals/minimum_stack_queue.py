from collections import deque
import math


class MinStack:
    def __init__(self):
        self.stack = deque()

    def __str__(self):
        arr = []
        for ele in self.stack:
            arr.append(ele)
        return str(arr)

    def push(self, val):
        self.stack.append((val, val if len(self.stack) == 0 else min(self.stack[-1][1], val)))

    def pop(self):
        return self.stack.pop()[0]

    def minimum(self):
        return self.stack[-1][1] if len(self.stack) else math.inf

    def empty(self):
        return len(self.stack) == 0


class MinQueue1:
    def __init__(self):
        self.stack = deque()

    def __str__(self):
        arr = []
        for ele in self.stack:
            arr.append(ele)
        return str(arr)

    def push(self, val):
        while not self.empty() and self.stack[0] > val:
            self.stack.popleft()
        self.stack.appendleft(val)

    def remove(self, val):
        if not self.empty() and self.stack[-1] == val:
            self.stack.pop()

    def minimum(self):
        return self.stack[-1] if len(self.stack) else math.inf

    def empty(self):
        return len(self.stack) == 0


class MinQueue2:
    def __init__(self):
        self.stack = deque()
        self.cnt_added = 0
        self.cnt_removed = 0

    def __str__(self):
        arr = []
        for ele in self.stack:
            arr.append(ele)
        return str(arr)

    def push(self, val):
        while not self.empty() and self.stack[0][0] > val:
            self.stack.popleft()
        self.stack.appendleft((val, self.cnt_added))
        self.cnt_added += 1

    def pop(self):
        if not self.empty() and self.stack[-1][1] == self.cnt_removed:
            ele = self.stack.pop()
        self.cnt_removed += 1

    def minimum(self):
        return self.stack[-1][0] if len(self.stack) else math.inf

    def empty(self):
        return len(self.stack) == 0


class MinQueue3:
    def __init__(self):
        self.in_stack = MinStack()
        self.out_stack = MinStack()

    def __str__(self):
        return str(self.in_stack) + str(self.out_stack)

    def push(self, val):
        self.in_stack.push(val)

    def pop(self):
        if not self.out_stack.empty():
            return self.out_stack.pop()
        elif not self.in_stack.empty():
            while not self.in_stack.empty():
                self.out_stack.push(self.in_stack.pop())
            return self.out_stack.pop()
        else:
            return None

    def minimum(self):
        if self.empty():
            return math.inf
        return min(self.in_stack.minimum(), self.out_stack.minimum())

    def empty(self):
        return self.in_stack.empty() and self.out_stack.empty()


def test_min(min_ds, arr, test_title):
    for ele in arr:
        min_ds.push(ele)
        print(f"Inserting: {ele}")
        print(f"{test_title}: {min_ds}")
        print(f"current min: {min_ds.minimum()}")

    ind = 0
    while not min_ds.empty():
        if test_title != 'queue1':
            min_ds.pop()
        else:
            min_ds.remove(arr[ind])
        print(f"{test_title}: {min_ds}")
        print(f"current min: {min_ds.minimum()}")
        ind += 1


def find_minimum_subarray(arr, ds, m):
    for i in range(m-1):
        ds.push(arr[i])

    result = []
    for i in range(m-1, len(arr)):
        ds.push(arr[i])
        result.append(ds.minimum())
        ds.pop()
    print(result)


def main():
    # min_stack = MinStack()
    min_queue2 = MinQueue2()
    min_queue3 = MinQueue3()
    arr = [9, 4, 12, 5, 1, 7, 9, 11, 3]
    # test_min(min_queue, arr, 'queue3')
    find_minimum_subarray(arr, min_queue2, 3)
    find_minimum_subarray(arr, min_queue3, 3)


if __name__ == '__main__':
    main()
