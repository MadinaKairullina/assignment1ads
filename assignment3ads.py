# Task 1
def two_sum(nums, target):
    hashmap = {}
    for i in range(len(nums)):
        need = target - nums[i]
        if need in hashmap:
            return [hashmap[need], i]
        hashmap[nums[i]] = i
print(two_sum([2,7,11,15], 9))
# Task 2
def first_uniq_char(s):
    count = {}
    for ch in s:
        count[ch] = count.get(ch, 0) + 1
    for i in range(len(s)):
        if count[s[i]] == 1:
            return i
    return -1
print(first_uniq_char("leetcode"))
# Task 3
def is_isomorphic(s, t):
    map1 = {}
    map2 = {}
    for a, b in zip(s, t):
        if a in map1 and map1[a] != b:
            return False
        if b in map2 and map2[b] != a:
            return False
        map1[a] = b
        map2[b] = a
    return True
print(is_isomorphic("egg","add"))
# Task 4
def is_happy(n):
    seen = set()
    while n != 1:
        if n in seen:
            return False
        seen.add(n)
        total = 0
        while n > 0:
            digit = n % 10
            total += digit * digit
            n //= 10
        n = total
    return True
print(is_happy(19))
# Task 5
from collections import deque
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
def level_order(root):
    if root is None:
        return []
    result = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result
root=TreeNode(3)
root.left=TreeNode(9)
root.right=TreeNode(20)
root.right.left=TreeNode(15)
root.right.right=TreeNode(7)
print(level_order(root))
# Task 6
def max_depth(root):
    if root is None:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
root=TreeNode(3)
root.left=TreeNode(9)
root.right=TreeNode(20)
root.right.left=TreeNode(15)
root.right.right=TreeNode(7)
print(max_depth(root))
# Task 7
def is_symmetric(root):
    def check(left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        return left.val==right.val and check(left.left,right.right) and check(left.right,right.left)
    if root is None:
        return True
    return check(root.left,root.right)
root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(2)
root.left.left=TreeNode(3)
root.left.right=TreeNode(4)
root.right.left=TreeNode(4)
root.right.right=TreeNode(3)
print(is_symmetric(root))
# Task 8
def longest_consecutive(root):
    if root is None:
        return 0
    max_len = 0
    def dfs(node, parent, length):
        nonlocal max_len
        if node is None:
            return
        if node.val == parent + 1:
            length += 1
        else:
            length = 1
        max_len = max(max_len, length)
        dfs(node.left, node.val, length)
        dfs(node.right, node.val, length)
    dfs(root, root.val - 1, 0)
    return max_len
root=TreeNode(1)
root.right=TreeNode(3)
root.right.left=TreeNode(2)
root.right.right=TreeNode(4)
root.right.right.right=TreeNode(5)
print(longest_consecutive(root))
# Task 9
def sort_colors(nums):
    left=0
    mid=0
    right=len(nums)-1
    while mid<=right:
        if nums[mid]==0:
            nums[left],nums[mid]=nums[mid],nums[left]
            left+=1
            mid+=1
        elif nums[mid]==1:
            mid+=1
        else:
            nums[mid],nums[right]=nums[right],nums[mid]
            right-=1
nums=[2,0,2,1,1,0]
sort_colors(nums)
print(nums)
# Task 10
def quick_sort(nums):
    def partition(low,high):
        pivot=nums[high]
        i=low-1
        for j in range(low,high):
            if nums[j]<=pivot:
                i+=1
                nums[i],nums[j]=nums[j],nums[i]
        nums[i+1],nums[high]=nums[high],nums[i+1]
        return i+1
    def sort(low,high):
        if low<high:
            p=partition(low,high)
            sort(low,p-1)
            sort(p+1,high)
    sort(0,len(nums)-1)
nums=[5,2,9,1,5,6]
quick_sort(nums)
print(nums)
# Task 11
def merge_sort(nums):
    if len(nums)<=1:
        return
    mid=len(nums)//2
    left=nums[:mid]
    right=nums[mid:]
    merge_sort(left)
    merge_sort(right)
    i=j=k=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            nums[k]=left[i]
            i+=1
        else:
            nums[k]=right[j]
            j+=1
        k+=1
    while i<len(left):
        nums[k]=left[i]
        i+=1;k+=1
    while j<len(right):
        nums[k]=right[j]
        j+=1;k+=1
nums=[5,2,9,1,5,6]
merge_sort(nums)
print(nums)
# Task 12
def heap_sort(nums):
    n=len(nums)
    def heapify(size,i):
        largest=i
        left=2*i+1
        right=2*i+2
        if left<size and nums[left]>nums[largest]:
            largest=left
        if right<size and nums[right]>nums[largest]:
            largest=right
        if largest!=i:
            nums[i],nums[largest]=nums[largest],nums[i]
            heapify(size,largest)
    for i in range(n//2-1,-1,-1):
        heapify(n,i)
    for i in range(n-1,0,-1):
        nums[0],nums[i]=nums[i],nums[0]
        heapify(i,0)
nums=[5,2,9,1,5,6]
heap_sort(nums)
print(nums)
