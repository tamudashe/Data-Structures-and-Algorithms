# Given an array of sorted numbers, remove all duplicates from it. You should not
# use anny extra space, after removing the duplicates in-place return the new
# length of the array

# Notes: right pointer moves to look for the next unique number
# left - 1 is the last unique number encountered

def remove_duplicates(nums):
    left = 1
    right = 1

    while right < len(nums):
        if nums[left - 1] != nums[right]:
            nums[left] = nums[right]
            left += 1
        right += 1

    return left

def main():
    nums = [1, 2, 4, 4, 5 , 6, 6, 7, 8, 8, 9, 9, 9, 10]
    print(remove_duplicates(nums))

if __name__ == '__main__':
    main()
