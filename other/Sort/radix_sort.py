import generate_and_assess as GA
from file_path import load_nums

# LSD 最低位开始排序
def counting_sort_for_radix(nums, exp):
    n = len(nums)
    output = [0]*n
    count = [0]*10
    for i in range(n):
        index = (nums[i]//exp)%10
        count[index] += 1

    for i in range(1,10):
        count[i] += count[i-1]

    for i in range(n-1,-1,-1):
        index = (nums[i]//exp)%10
        output[count[index]-1] = nums[i]
        count[index] -= 1

    for i in range(n):
        nums[i] = output[i]


def radix_sort(nums):
    if nums == []:
        return []
    max_num = max(nums)

    exp = 1
    while max_num//exp > 0:
        counting_sort_for_radix(nums,exp)
        exp *= 10
    return nums


def main():
    nums1, nums2 = load_nums()

    GA.test_sort('LSD基数排序全随机',radix_sort,nums1)
    GA.test_sort('LSD基数排序部分有序',radix_sort,nums2)


if __name__ == '__main__':
    main()






