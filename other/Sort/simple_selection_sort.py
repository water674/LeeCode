import generate_and_assess as GA
from file_path import load_nums


def simple_selection_sort(nums):
    n = len(nums)
    for i in range(n-1,-1,-1):
        j = nums[0:i+1].index(max(nums[0:i+1]))
        nums[i],nums[j] = nums[j],nums[i]
    return nums


def main():
    nums1, nums2 = load_nums()
    GA.test_sort('简单选择排序全随机',simple_selection_sort,nums1)
    GA.test_sort('简单选择排序部分有序',simple_selection_sort,nums2)


if __name__ == '__main__':
    main()