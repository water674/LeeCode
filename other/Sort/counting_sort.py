import generate_and_assess as GA
from file_path import load_nums

def counting_sort(arr):

    max_val = max(arr) if arr else 0
    count = [0] * (max_val + 1)
    
    for num in arr:
        count[num] += 1
    
    result = []
    
    for i in range(len(count)):
        result.extend([i] * count[i])
    
    return result



def main():
    nums1, nums2 = load_nums()

    GA.test_sort('计数排序全随机',counting_sort,nums1)
    GA.test_sort('计数排序部分有序',counting_sort,nums2)


if __name__ == '__main__':
    main()
