import generate_and_assess as GA
from file_path import load_nums

def shell_sort(nums):
    n = len(nums)
    gap = n//2

    while gap > 0:
        for i in range(gap,n):
            temp = nums[i]
            j = i
            while j >= gap and nums[j - gap] > temp:
                nums[j] = nums[j - gap]
                j -= gap
            
            nums[j] = temp

        gap = gap//2
    return nums


def main():
    nums1, nums2 = load_nums()
    
    GA.test_sort('希尔排序全随机',shell_sort,nums1)
    GA.test_sort('希尔排序部分有序',shell_sort,nums2)


if __name__ == '__main__':
    main()

