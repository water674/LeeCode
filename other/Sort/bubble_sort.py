import generate_and_assess as GA
from file_path import load_nums


def bubble_sort(nums):
    n = len(nums)
    for j in range(n-1,-1,-1):
        for i in range(j):
            if nums[i] >= nums[i+1]:
                nums[i],nums[i+1] = nums[i+1],nums[i]
    return nums


def main():
    nums1, nums2 = load_nums()
    
    GA.test_sort('冒泡排序全随机',bubble_sort,nums1)
    GA.test_sort('冒泡排序部分有序',bubble_sort,nums2)


if __name__ == '__main__':
    main()