'''

Problem:
https://leetcode.com/problems/peeking-iterator/


'''


'''

Approach:
Store a buffer which essentially holds the data at the current itr position
it additionally serves to tell us if there is a next piece of data


'''


# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator(object):
    def __init__(self, iterator):
        self.iterator = iterator
        self.buffer = None

        if iterator.hasNext():
            self.buffer = iterator.next()
        

    def peek(self):
        return self.buffer
        

    def next(self):
        val = self.buffer

        self.buffer = self.iterator.next() if self.iterator.hasNext() else None

        return val
        

    def hasNext(self):
        return self.buffer is not None
    


"""

Time Complexity:

init: O(1)
peek: O(1)
next: O(1)
hasNext: O(1)

Overall ---> all operations are O(1)

Space Complexity:
just stores the next item in the data so overall ---> O(1)


"""