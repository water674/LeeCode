## 十种排序算法

本文记录了十大经典的排序算法,总结来自 https://www.runoob.com/w3cnote/ten-sorting-algorithm.html 仅作为平时记录自己学习过程用途

代码部分由本人亲自手写,有问题望告知。

其中[file_path.py](https://github.com/water674/Zergen.X/blob/%E6%8E%92%E5%BA%8F/file_path.py)文件表示保存的文件路径;[generate_and_assess.py]([https://github.com/water674/Zergen.X/blob/%E6%8E%92%E5%BA%8F/generate_and_assess.py](https://github.com/water674/LeeCode/blob/main/other/Sort/generate_and_assess.py))文件有生成随机数组,判断排序是否成功和排序所用时间的功能.

  | 排序算法     | 平均时间复杂度 | 最好情况        | 最坏情况          | 空间复杂度     |   排序方式   | 稳定性   |
  | ------------ | ------------- | -------------  | -----------------| -----------   | ---------    | --------|
  | 冒泡排序     | $O(n^2)$       | $O(n)$         |  $O(n^2)$        | $O(1)$        | In-place     | 稳定     |
  | 简单选择排序  |$O(n^2)$       | $O(n^2)$       |  $O(n^2)$         | $O(1)$       | In-place     | 不稳定   | 
  | 插入排序     | $O(n^2)$       | $O(n)$         | $O(n^2)$          | $O(1)$       | In-place     | 稳定     |
  | 希尔排序     | $O(n \log n)$  |$O(n \log^{2}n)$|$O(n \log^{2}n)$   | $O(1)$       | In-place     | 不稳定   | 
  | 归并排序     |$O(n \log n)$   | $O(n \log n)$  | $O(n \log n)$     | $O(n)$       | Out-place    | 稳定     |
  | 快速排序     | $O(n \log n)$  | $O(n \log n)$  | $O(n^2)$          | $O(n \log n)$| In-place     | 不稳定   | 
  | 堆排序       |$O(n \log n)$   |$O(n \log n)$   | $O(n \log n)$     | $O(1)$       | In-place     | 不稳定   | 
  | 计数排序     | $O(n+k)$       | $O(n+k)$       | $O(n+k)$          | $O(k)$       | Out-place    | 稳定     | 
  | 桶排序       | $O(n+k)$       | $O(n+k)$       | $O(n^2)$          | $O(n+k)$     | Out-place    | 稳定     |
  | 基数排序     | $O(n \times k)$| $O(n \times k)$| $O(n \times k)$   | $O(n+k)$     | Out-place    | 稳定     | 
