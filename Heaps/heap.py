# Heap - specialized binary tree (complete binary tree)
# [max-heap] - key at each node >= keys stored at its children
# [min-heap] - key at each node <= keys stored at its children
# heap can be implemented as an array
# children of node at index (i) are at indices (2i + 1) and (2i + 2)

# inserting element     : O(log n)
# deleting element      : O(log n)
# lookup for max element: O(1)
# searching for element : O(n)

# the extract-max operation is defined to delete and return the maximum element
# heap: sometimes referred to as a priority queue, because it behaves like a queue
# with one difference:each element has a 'priority' associated with it and
# deletion removes the element with the highest priority

# min-heap : same except the lowest values has highest piority

# use the heap when all you care about is the largest or smallest elements, and
# you do not need to support fast lookup, delete or search operations for
# arbitrary elements

# a heap is a good choice when you need to compute the  k largest
# or k smallest elements in a collection.

# heap libraries: heapq module
# heapq: only provides min-heap functionality
# heapq.heapify(L): transforms elements in L into a heap in-place
# heapq.nlargest(k, L) heapq.nsmallest(k, L): returnd the k largest or smalest elements in L
# heapq.heappush(h, e): pushes a new element on the heap
# heapq.heappop(h): pops the smallest element from the heap
# heapq.heappushpop(h, a): pushes a on the heap and pops and returns the smallest element
# e = h[0]: returns the smallest element on the heap without poping it

# to build a max-heap on integers or floats, insert their negative to get effect
# of a max-heap using heapq.
# -------------------------------------------------------------------------------
# Q1 Write a program that takes as input a set of sorted sequences and computes
# the union of these sequences as a sorted sequence.
# input : [[3, 5, 7], [0, 6], [0, 6, 28]]
# output: [0, 0, 3, 5, 6, 7, 28]
import heapq

def sort_files(files):
    return list(heapq.merge(*files))

def main():
    files = [[3, 5, 7], [0, 6], [0, 6, 28]]
    print(sort_files(files))

if __name__ == '__main__':
    main()
