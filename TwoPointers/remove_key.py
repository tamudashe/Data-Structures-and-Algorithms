# Given an unsorted array of numbers and a 'key', remove all instances of 'key'
# in-place and return the new length of the array

def remove_key(nums, key):
    left = 0
    for num in nums:
        if num != key:
            nums[left] = num
            left += 1
    return left

def main():
    nums = [2, 4, 3, 3, 1, 2, 4, 6, 7, 9, 5, 7, 3, 2]
    key = 2
    print(remove_key(nums, key))

if __name__ == '__main__':
    main()
