import generate_and_assess as GA
from file_path import load_nums


def insertion_sort(nums):
    n = len(nums)
    for i in range(1,n):
        l,r = 0,i-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == nums[i]:
                index = mid
                break
            elif nums[mid] > nums[i]:
                r = mid-1
            else:
                l = mid+1
        else:
            index = l
            
        for j in range(i-1,index-1,-1):
            nums[j],nums[j+1] = nums[j+1],nums[j]
    
    return nums


def main():
    nums1, nums2 = load_nums()
    
    GA.test_sort('插入排序全随机',insertion_sort,nums1)
    GA.test_sort('插入排序部分有序',insertion_sort,nums2)


if __name__ == '__main__':
    main()