# 1
def print_1_to_n(n):
    if n == 0:
        return
    print_1_to_n(n - 1)
    print(n, end=" ")

n = int(input())
print_1_to_n(n)
print()
#Space:O(n) Time:O(n)

# 2
def print_n_to_1(n):
    if n == 0:
        return
    print(n, end=" ")
    print_n_to_1(n - 1)

n = int(input())
print_n_to_1(n)
print()
#Space:O(n) Time:O(n)

# 3
def sum_n(n):
    if n == 1:
        return 1
    return n + sum_n(n - 1)

n = int(input())
print(sum_n(n))
#Space:O(n) Time:O(n)

# 4
def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)

n = int(input())
print(fact(n))
#Space:O(n) Time:O(n)

# 5
def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)

a = int(input())
b = int(input())
print(power(a, b))
#Space:O(n) Time:O(n)

# 6
def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)

n = int(input())
print(sum_digits(n))


# 7
def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)

n = int(input())
print(count_digits(n))


# 8
def reverse_num(n):
    if n == 0:
        return
    print(n % 10, end="")
    reverse_num(n // 10)

n = int(input())
reverse_num(n)
print()


# 9
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

n = int(input())
print(fib(n))
#Space:O(n) Time:O(n^2)

# 10
def is_pal(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_pal(s[1:-1])

s = input()
if is_pal(s):
    print("Palindrome")
else:
    print("Not palindrome")
#Space:O(n^2) Time:O(n^2)

# 11
def sum_array(arr, i=0):
    if i == len(arr):
        return 0
    return arr[i] + sum_array(arr, i + 1)

arr = list(map(int, input().split()))
print(sum_array(arr))
#Space:O(n) Time:O(n)

# 12
def max_array(arr, i=0):
    if i == len(arr) - 1:
        return arr[i]
    m = max_array(arr, i + 1)
    return arr[i] if arr[i] > m else m

arr = list(map(int, input().split()))
print(max_array(arr))
#Space:O(n) Time:O(n)

# 13
def count_target(arr, target, i=0):
    if i == len(arr):
        return 0
    count = 1 if arr[i] == target else 0
    return count + count_target(arr, target, i + 1)

arr = list(map(int, input().split()))
t = int(input())
print(count_target(arr, t))
#Space:O(n) Time:O(n)

# 14
def search(arr, target, i=0):
    if i == len(arr):
        return False
    if arr[i] == target:
        return True
    return search(arr, target, i + 1)

arr = list(map(int, input().split()))
t = int(input())
if search(arr, t):
    print("Found")
else:
    print("Not found")
#Space:O(n) Time:O(n)

# 15
def is_sorted(arr, i=0):
    if i == len(arr) - 1:
        return True
    if arr[i] > arr[i + 1]:
        return False
    return is_sorted(arr, i + 1)

arr = list(map(int, input().split()))
if is_sorted(arr):
    print("Sorted")
else:
    print("Not sorted")
#Space:O(n) Time:O(n)

# 16
def binary_search(arr, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return binary_search(arr, target, left, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, right)

arr = list(map(int, input().split()))
t = int(input())
res = binary_search(arr, t, 0, len(arr) - 1)
if res != -1:
    print("Element found at index", res)
else:
    print("Not found")
#Space:O(log(n)) Time:O(log(n))
