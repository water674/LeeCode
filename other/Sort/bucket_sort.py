import generate_and_assess as GA
from file_path import load_nums
import radix_sort


def bucket_sort(nums):
    # 桶排序和桶的个数息息相关,一般要看看数据上下界和分布
    n = len(nums)
    max_value = max(nums)
    count_buckets = (max_value//10)+1
    buckets = [[] for _ in range(count_buckets)]
    for i in range(n):
        index = nums[i]//10
        buckets[index].append(nums[i])
    
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(radix_sort.radix_sort(bucket))# 桶内使用一种排序算法,我为了方便,随便加的前一个写的基数排序

    return sorted_array



def main():
    nums1, nums2 = load_nums()

    GA.test_sort('桶排序全随机',bucket_sort,nums1)
    GA.test_sort('桶排序部分有序',bucket_sort,nums2)


if __name__ == '__main__':
    main()