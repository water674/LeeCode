# [力扣28](https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/description/?envType=study-plan-v2&envId=top-interview-150)

给你两个字符串 `haystack` 和 `needle`，请你在 `haystack` 字符串中找出 `needle` 字符串的第一个匹配项的下标(下标从 0 开始)。如果 `needle` 不是 `haystack` 的一部分，则返回 -1 。

示例 1：

输入: `haystack` = "sadbutsad", `needle` = "sad"

输出：0

解释："sad" 在下标 0 和 6 处匹配。第一个匹配项的下标是 0 ，所以返回 0 。

示例 2:

输入: `haystack` = "leetcode", `needle` = "leeto"

输出： -1

解释: "leeto" 没有在 "leetcode" 中出现，所以返回 -1。

提示：

-  $1<=$  `haystack`.length, `needle`.length $<=10^{4}$
- `haystack` 和 `needle` 仅由小写英文字符组成

## 对于朴素写法为：

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        for i in range(n):
            if i+m<=n:
                window = haystack[i:i+m]
                if window == needle:
                    return i
        return -1
```
时间复杂度：O(m*n)

空间复杂度：O(1)


## 改造为双指针的形式,为了方便KMP的编写：
```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        i,j = 0,0
        while i<n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == m:
                    return i-j
            else:
                i = i-j+1
                j = 0
        return -1
```

## KMP版本：
```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        i = j = 0

        def longest_length_of_prefix_and_suffix(substr):
            n = len(substr)
            if n == 1:
                return 0
            num = 0
            for i in range(n-1):
                if substr[:n-i-1] == substr[i+1:]:
                    num = len(substr[i+1:])
                    break
            return num

        def getnext(needle):
            m = len(needle)
            next = [0]*m
            if m == 1:
                next = [0]
            elif m == 2:
                next = [0,1]
            else:
                next[1] = 1
                for i in range(2,m):
                    next[i] = longest_length_of_prefix_and_suffix(needle[0:i])+1
            return next

        next = getnext(needle)

        while i < n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == m:
                    return i - j
            else:
                if j > 0:
                    j = next[j]-1
                else:
                    i += 1
                    j = 0
        return -1
```
时间复杂度：O(m+n)

空间复杂度：O(m) , m为`needle`的长度





## KMP优化版本('史山',但好理解)：

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        i = j = 0

        def longest_length_of_prefix_and_suffix(substr):
            n = len(substr)
            if n == 1:
                return 0
            num = 0
            for i in range(n-1):
                if substr[:n-i-1] == substr[i+1:]:
                    num = len(substr[i+1:])
                    break
            return num

        def getnext(needle):
            m = len(needle)
            next = [0]*m
            if m == 1:
                next = [0]
            elif m == 2:
                next = [0,1]
            else:
                next[1] = 1
                for i in range(2,m):
                    next[i] = longest_length_of_prefix_and_suffix(needle[0:i])+1
            return next

        next = getnext(needle)
 
        def getnextval(needle,next):
            nextval = next
            for i in range(1,len(next)):
                if needle[i] == needle[next[i]-1]:
                    nextval[i] = next[next[i]-1]
            return nextval
        
        nextval = getnextval(needle,next)

        while i < n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == m:
                    return i - j
            else:
                if j > 0:
                    j = nextval[j]-1
                else:
                    i += 1
                    j = 0
        return -1
```



## 终极版本(修改代码结构,看起来更漂亮)：

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)

        next = [0] * m
        j = 0
        for i in range(1, m):
            while j > 0 and needle[i] != needle[j]:
                j = next[j - 1]
            if needle[i] == needle[j]:
                j += 1
            next[i] = j

        i = j = 0
        while i < n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == m:
                    return i - j
            else:
                if j > 0:
                    j = next[j - 1]
                else:
                    i += 1
        
        return -1

```


***
***


# KMP算法适用于匹配子串的场景

契机：对于朴素算法,每次都要比较长串的子串和短串是否一样,相当于如果一旦匹配不成功,都只是把窗口往右移动一格,且j从头开始继续匹配,这个过程循环下去.如果有一个数组 `next` 能够告诉我匹配不成功的时候我应该往右移动几格或者告诉我j能不能不要每次都从头开始,应该从哪开始就好了.

## 如果有了 `next` 数组应该怎么写代码呢？

比如对于 `haystack` = "sadbutsad", `needle` = "sad"

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        i = j = 0
        next = [0,1,1] # 至于怎么求的先不管,直接告诉你就是这个
        while i < n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == m:
                    return i - j
            else:
                if j > 0:
                    j = next[j]-1
                else:
                    i += 1
                    j = 0
        return -1
```

## 怎么求 `next` 数组呢？
证明略。

直接告诉求next[j]方法如下：1~j-1构成的字串的最长相等前后缀的长度加1,特别的：`next[1]`=0,`next[2]`=1

```
例1：`aaaab`

`next[3]`:  子串为`aa` 前缀：`a`  后缀：`a`  因此最长相等前后缀长度为1,`next[3]` = 1+1 = 2

`next[4]`:  子串为`aaa` 前缀：`aa`  后缀：`aa`  因此最长相等前后缀长度为2,`next[4]` = 2+1 = 3

`next[5]`:  子串为`aaaa` 前缀：`aaa`  后缀：`aaa`  因此最长相等前后缀长度为3,`next[5]` = 3+1 = 4
```

```
例2：`sad`

`next[3]`:  子串为`sa` 前缀：`s`  后缀：`a`  因此最长相等前后缀长度为0,`next[3]` = 0+1 = 1 也就对应上了上述代码块中的`next`
```


```
例3：`ababaa`

`next[3]`:  子串为`ab` 前缀：`a`  后缀：`b`  因此最长相等前后缀(` `)长度为0,`next[3]` = 0+1 = 1

`next[4]`:  子串为`aba` 前缀：`ab`  后缀：`ba`  因此最长相等前后缀(`a`)长度为1,`next[4]` = 1+1 = 2

`next[5]`:  子串为`abab` 前缀：`aba`  后缀：`bab`  因此最长相等前后缀(`ab`)长度为2,`next[5]` = 2+1 = 3

`next[6]`:  子串为`ababa` 前缀：`abab`  后缀：`baba`  因此最长相等前后缀(`aba`)长度为3,`next[6]` = 3+1 = 4
```

```
例4：`abaabc`

`next[3]`:  子串为`ab` 前缀：`a`  后缀：`b`  因此最长相等前后缀(` `)长度为0,`next[3]` = 0+1 = 1

`next[4]`:  子串为`aba` 前缀：`ab`  后缀：`ba`  因此最长相等前后缀(`a`)长度为1,`next[4]` = 1+1 = 2

`next[5]`:  子串为`abaa` 前缀：`aba`  后缀：`baa`  因此最长相等前后缀(`a`)长度为1,`next[5]` = 1+1 = 2

`next[6]`:  子串为`abaab` 前缀：`abaa`  后缀：`baab`  因此最长相等前后缀长度为2,`next[6]` = 2+1 = 3
```



```python
def longest_length_of_prefix_and_suffix(substr):
    n = len(substr)
    if n == 1:
        return 0
    num = 0
    for i in range(n-1):
        if substr[:n-i-1] == substr[i+1:]:
            num = len(substr[i+1:])
            break
    return num

def getnext(needle):
    m = len(needle)
    next = [0]*m
    if m == 1:
        next = [0]
    elif m == 2:
        next = [0,1]
    else:
        next[1] = 1
        for i in range(2,m):
            next[i] = longest_length_of_prefix_and_suffix(needle[0:i])+1
    return next
```

因此合起来就有了[1.找出字符串第一个匹配的下标](https://github.com/water674/Zergen.X----Data-Structures-and-Algorithms/blob/%E5%8A%9B%E6%89%A3/KMP/1.%E6%89%BE%E5%87%BA%E5%AD%97%E7%AC%A6%E4%B8%B2%E7%AC%AC%E4%B8%80%E4%B8%AA%E5%8C%B9%E9%85%8D%E7%9A%84%E4%B8%8B%E6%A0%87.md)里的KMP版本。


## 有没有优化方式呢？
比如对于上面例4而言：`abaabc`,`next` = [0,1,1,2,2,3].很明显，如果j=3没有匹配上,则由`next`告诉得应该回溯到j=1,注意到第1个和第3个都是`a`,而j=3没有匹配上意味着长串对应位置不可能是`a`,因此所以可以直接令`next[3]`=`next[1]`=0去.同理：`next[5]` = `next[2]` = 1.所以优化后的`nextval`= [0,1,0,2,1,3].

注意：`next[4]`不能优化了,因为`next[4]`= 2,而第4个(`a`)和第2个(`b`)不一样.

再比如例3：`next`=[0,1,1,2,3,4],优化后为`nextval`=[0,1,0,1,0,4].

再直接给出一个例子：`aaaab`的`next` = [0,1,2,3,4],`nextval` = [0,0,0,0,4].

```python
def getnextval(needle,next):
    nextval = next
    for i in range(1,len(next)):
        if needle[i] == needle[next[i]-1]:
            nextval[i] = next[next[i]-1]
    return nextval
```


## 说了这么多，终极版本是？

简化求前缀后缀以及修改`next`的结构使得只要索引正确就行

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)

        next = [0] * m
        j = 0
        for i in range(1, m):
            while j > 0 and needle[i] != needle[j]:
                j = next[j - 1]
            if needle[i] == needle[j]:
                j += 1
            next[i] = j

        i = j = 0
        while i < n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == m:
                    return i - j
            else:
                if j > 0:
                    j = next[j - 1]
                else:
                    i += 1
        
        return -1

```




































