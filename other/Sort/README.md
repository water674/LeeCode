## 十种排序算法

本文记录了十大经典的排序算法,总结来自 https://www.runoob.com/w3cnote/ten-sorting-algorithm.html 仅作为平时记录自己学习过程用途

代码部分由本人亲自手写,有问题望告知。

其中[file_path.py](https://github.com/water674/Zergen.X/blob/%E6%8E%92%E5%BA%8F/file_path.py)文件表示保存的文件路径;[generate_and_assess.py](https://github.com/water674/Zergen.X/blob/%E6%8E%92%E5%BA%8F/generate_and_assess.py)文件有生成随机数组,判断排序是否成功和排序所用时间的功能.

  | 排序算法     | 平均时间复杂度 | 最好情况        | 最坏情况          | 空间复杂度     |   排序方式   | 稳定性   |    链接   |
  | ------------ | ------------- | -------------  | -----------------| -----------   | ---------    | --------| -------- |
  | 冒泡排序     | $O(n^2)$       | $O(n)$         |  $O(n^2)$        | $O(1)$        | In-place     | 稳定     | [bubble_sort.py](https://github.com/water674/Zergen.X/blob/%E6%8E%92%E5%BA%8F/bubble_sort.py)|
  | 简单选择排序  |$O(n^2)$       | $O(n^2)$       |  $O(n^2)$         | $O(1)$       | In-place     | 不稳定   | [simple_selection_sort.py](https://github.com/water674/Zergen.X/blob/%E6%8E%92%E5%BA%8F/simple_selection_sort.py) |
  | 插入排序     | $O(n^2)$       | $O(n)$         | $O(n^2)$          | $O(1)$       | In-place     | 稳定     | [insertion_sort.py](https://github.com/water674/Zergen.X/blob/%E6%8E%92%E5%BA%8F/insertion_sort.py) |
  | 希尔排序     | $O(n \log n)$  |$O(n \log^{2}n)$|$O(n \log^{2}n)$   | $O(1)$       | In-place     | 不稳定   | [sheel_sort.py](https://github.com/water674/Zergen.X/blob/%E6%8E%92%E5%BA%8F/shell_sort.py) |
  | 归并排序     |$O(n \log n)$   | $O(n \log n)$  | $O(n \log n)$     | $O(n)$       | Out-place    | 稳定     | [merge_sort.py](https://github.com/water674/Zergen.X/blob/%E6%8E%92%E5%BA%8F/merge_sort.py) |
  | 快速排序     | $O(n \log n)$  | $O(n \log n)$  | $O(n^2)$          | $O(n \log n)$| In-place     | 不稳定   | [quick_sort.py](https://github.com/water674/Zergen.X/blob/%E6%8E%92%E5%BA%8F/quick_sort.py) |
  | 堆排序       |$O(n \log n)$   |$O(n \log n)$   | $O(n \log n)$     | $O(1)$       | In-place     | 不稳定   | [heap_sort.py](https://github.com/water674/Zergen.X----Data-Structures-and-Algorithms/blob/%E6%8E%92%E5%BA%8F/heap_sort.py) |
  | 计数排序     | $O(n+k)$       | $O(n+k)$       | $O(n+k)$          | $O(k)$       | Out-place    | 稳定     | [counting_sort.py](https://github.com/water674/Zergen.X----Data-Structures-and-Algorithms/blob/%E6%8E%92%E5%BA%8F/counting_sort.py) |
  | 桶排序       | $O(n+k)$       | $O(n+k)$       | $O(n^2)$          | $O(n+k)$     | Out-place    | 稳定     | [bucket_sort.py](https://github.com/water674/Zergen.X----Data-Structures-and-Algorithms/blob/%E6%8E%92%E5%BA%8F/bucket_sort.py) |
  | 基数排序     | $O(n \times k)$| $O(n \times k)$| $O(n \times k)$   | $O(n+k)$     | Out-place    | 稳定     | [radix_sort.py](https://github.com/water674/Zergen.X----Data-Structures-and-Algorithms/blob/%E6%8E%92%E5%BA%8F/radix_sort.py) |


