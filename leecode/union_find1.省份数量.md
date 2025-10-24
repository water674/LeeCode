# [力扣547](https://leetcode.cn/problems/number-of-provinces/description/)
```
有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。
省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。
给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，
而 isConnected[i][j] = 0 表示二者不直接相连。
返回矩阵中 省份 的数量。
```

```
示例 1：
输入：isConnected = [[1,1,0],[1,1,0],[0,0,1]]
输出：2

示例 2：
输入：isConnected = [[1,0,0],[0,1,0],[0,0,1]]
输出：3
```
```
提示：
1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] 为 1 或 0
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]
```



```python
#并查集
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        fa = [i for i in range(n)]

        def find(x):
            nonlocal fa
            if fa[x] == x:
                return x
            return find(fa[x])


        def union(x,y):
            nonlocal fa
            fax = find(x)
            fay = find(y)
            if fax == fay:
                return
            else:
                fa[fax] = fay

        for i in range(n):
            for j in range(i+1,n):
                if isConnected[i][j] == 1:
                    union(i,j)


        return len(set(find(i) for i in range(n)))

```
```python
# 图的dfs
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False]*n

        def dfs(u):
            visited[u] = True
            for i in range(n):
                if i != u and isConnected[i][u] == 1 and not visited[i]:
                    visited[i] = True
                    dfs(i)
        res = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                res += 1
        return res
```
