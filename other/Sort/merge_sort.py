import generate_and_assess as GA
from file_path import load_nums


def merge_two_sorted_arr(nums1,nums2):
    m,n = len(nums1),len(nums2)
    p1,p2 = 0,0
    nums = []
    while p1<m and p2<n:
        if nums1[p1]<nums2[p2]:
            nums.append(nums1[p1])
            p1 += 1
        else:
            nums.append(nums2[p2])
            p2 += 1
    if p1 == m:
        while p2<n:
            nums.append(nums2[p2])
            p2 += 1
    elif p2 == n:
        while p1<m:
            nums.append(nums1[p1])
            p1 += 1
    return nums


def merge_sort(nums):
    n = len(nums)
    if n == 1:
        return nums
    nums1 = merge_sort(nums[:n//2])
    nums2 = merge_sort(nums[n//2:])
    nums = merge_two_sorted_arr(nums1,nums2)
    return nums


def main():
    nums1, nums2 = load_nums()
    
    GA.test_sort('归并排序全随机',merge_sort,nums1)
    GA.test_sort('归并排序部分有序',merge_sort,nums2)


if __name__ == '__main__':
    main()