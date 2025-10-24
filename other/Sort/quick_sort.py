import generate_and_assess as GA
from file_path import load_nums

def quick_sort(nums):
    n = len(nums)
    if n <= 1:
        return nums
    pivot = nums[0]
    i,j = 1,n-1
    while i <= j:
        while i<=j and nums[i] <= pivot:
            i += 1
        while i<=j and nums[j] > pivot:
            j -= 1
        if i<j:
            nums[i],nums[j] = nums[j],nums[i]
    nums[j],nums[0] = nums[0],nums[j]

    return quick_sort(nums[:j]) + [pivot] + quick_sort(nums[j+1:])


def main():
    nums1, nums2 = load_nums()
    
    GA.test_sort('快速排序全随机',quick_sort,nums1)
    GA.test_sort('快速排序部分有序',quick_sort,nums2)


if __name__ == '__main__':
    main()