import random
import time
import pickle
import file_path
file_path = file_path.file_path()

def generate(n):
    return [random.randint(0,n) for _ in range(n)]

# 生成一个近乎有序的数组.swap_times 的作用是控制在生成的近乎有序数组中随机交换元素的次数.
def generate_nearly_ordered_array(n,swap_times):
    nums = list(range(0,n + 1))
    for _ in range(swap_times):
        pos_x = random.randint(0, n - 1)
        pos_y = random.randint(0, n - 1)
        nums[pos_x], nums[pos_y] = nums[pos_y], nums[pos_x]
    return nums


def is_sorted(nums):
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True


def test_sort(sort_name, sort_function, nums):
    start_time = time.time()
    sorted_nums = sort_function(nums)
    end_time = time.time()

    print(f"{'是否有序'}: {is_sorted(sorted_nums)}")
    print(f"{sort_name}: {end_time - start_time:.25f} seconds")


def main(n):
    nums1 = generate(n)
    nums2 = generate_nearly_ordered_array(n,n//4)
    with open(file_path, 'wb') as f:
        pickle.dump((nums1, nums2), f)

if __name__ == '__main__':
    n = 10**4
    main(n)
    print('+--------------------------------+')
    print('|已保存至文件 generated_data.pkl |')
    print('+--------------------------------+')