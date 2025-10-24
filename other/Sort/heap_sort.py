class MaxHeap():  # 大根堆 
    def __init__(self,nums):
        self.nums = nums
        self.build_max_heap()

    def build_max_heap(self):
        nums = self.nums
        n = len(nums)
        for i in range(n//2-1,-1,-1):
            self.heap_adjust(i,n)

    def heap_adjust(self,k,n):
        nums = self.nums
        temp = nums[k]
        i = 2*k+1
        while i<n:
            if i<n-1 and nums[i]<nums[i+1]:
                i += 1
            if temp >= nums[i]:
                break
            else:
                nums[k]=nums[i]
                k = i
                i = 2*k+1
        nums[k] = temp

def heap_sort(nums):
    heap = MaxHeap(nums)
    n = len(nums)
    for i in range(n-1,0,-1):
        nums[0],nums[i] = nums[i],nums[0]
        heap.heap_adjust(0,i)
    return nums

import generate_and_assess as GA
from file_path import load_nums

def main():
    nums1, nums2 = load_nums()
    
    GA.test_sort('堆排序全随机',heap_sort,nums1)
    GA.test_sort('堆排序部分有序',heap_sort,nums2)


if __name__ == '__main__':
    main()




######################################################################################
class MinHeap():  # 小根堆
    def __init__(self,nums):
        self.nums = nums
        self.build_min_heap()

    def build_min_heap(self):
        nums = self.nums
        n = len(nums)
        for i in range(n//2-1,-1,-1):
            self.heap_adjust(i,n)

    def heap_adjust(self,k,n):
        nums = self.nums
        temp = nums[k]
        i = 2*k+1
        while i<n:
            if i<n-1 and nums[i] >= nums[i+1]:
                i += 1
            if temp <= nums[i]:
                break
            else:
                nums[k]=nums[i]
                k = i
                i = 2*k+1
        nums[k] = temp


