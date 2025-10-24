# [力扣739](https://leetcode.cn/problems/daily-temperatures/description/)

```
给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，其中 answer[i] 是指对于第 i 天，
下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用 0 来代替。
```
```
示例 1:
输入: temperatures = [73,74,75,71,69,72,76,73]
输出: [1,1,4,2,1,1,0,0]

示例 2:
输入: temperatures = [30,40,50,60]
输出: [1,1,1,0]

示例 3:
输入: temperatures = [30,60,90]
输出: [1,1,0]
```
```
提示：
1 <= temperatures.length <= 10**5
30 <= temperatures[i] <= 100
```

```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        nums = temperatures
        res = [0]*n
        for i in range(n):
            if not stack or nums[i]<nums[stack[-1]]:
                stack.append(i)
            else:
                while stack and nums[i]> nums[stack[-1]]:
                    tmp = stack.pop()
                    res[tmp] = i-tmp
                stack.append(i)
        return res


```
