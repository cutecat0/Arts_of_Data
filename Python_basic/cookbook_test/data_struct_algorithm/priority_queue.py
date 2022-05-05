import heapq

"""
    Q: How to bring a priority queue & each time of 'POP' operation
    can return the most high priority one on this queue?

    A: use heapq
"""


class PriorityQueue:

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


if __name__ == '__main__':
    q = PriorityQueue()
    q.push(Item('Cat'), 10)
    q.push(Item('Rabbit'), 8)
    q.push(Item('Dog'), 10)
    q.push(Item('Food'), 1)

    print(q)
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())
