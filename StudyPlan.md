# Coding interviews study plan

- Programming language: Python 3

1; Python Basics

- all necessary libraries
  collections module

  `for i in range(numbers)`
  `for i in reversed(numbers)`
  `for index, value in enumerate(numbers)`
  `for name, number in zip(names, numbers)`
  `for i in sorted(numbers)`
  `for i in sorted(numbers, reverse=True)`
  `sorted(names, key=len)`

- using 2D arrays
- reading writing from files
- memory management in python

2; Data structures and algorithms

- Primitive types

- Arrays & Strings

  Always ask if string is ASCII(128), Extended ASCII(256) or Unicode
  Always ask if string is case sensitive
  Always ask if white space affects two different strings

  ASCII string : uses 8-bit encoding
    ASCII: 128 Extended ASCII: 256
  Unicode string : uses variable bit encoding
  string and array questions are often interchangeable
  * resizing factor of lists in python
  Why is the amortized insertion runtime 0(1)? - resizes happen very rarely
  Inserting N elements takes O(N) work
  * consider using a bit array / bit map / bit string
  * bit masking
  * counting bits set to 1

  Always ask if
- Linked lists
- Stacks and queues
- Binary trees
- Heaps
- Searching

- Hash tables
  can be represented using an array of linked lists or a binary search tree
  array of linked lists worst case: lookup = O(N)
  binary search tree: lookup = O(log N) -> uses less space -> order is maintained

- Sorting
- Binary search trees
- Recursion
- Dynamic programming
- Greedy algorithms and Invariants
- Graphs

### Programming interview Patterns
__

1. Sliding Window
2. Two Pointers
3. Fast & Slow pointers
4. Merge Intervals
5. Cyclic Sort
6. In-place Reversal of a LinkedList
7. Tree Breadth First Search
8. Tree Depth First Search
9. Two Heaps
10. Subsets
11. Modified Binary Search
12. Bitwise XOR
13. Top 'K' Elements
15. K-way merge
16. 0/1 Knapsack (Dynamic Programming)
17. Topological Sort (Graph)

__
