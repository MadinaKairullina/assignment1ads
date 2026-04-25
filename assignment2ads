#1
def add_to_start(lst):
    a = input()
    if a.isdigit():
        a = int(a)
    lst.insert(0, a)
    return lst
list = [1,2,3]
list = add_to_start(list)
print(list)
#2
def add_to_end(lst):
    a = input()
    if a.isdigit():
        a = int(a)
    lst.append(a)
    return lst
list = [1,2,3]
list = add_to_start(list)
print(list)
#3
def remove_last(lst):
    if len(lst) > 0:
        lst.pop()
    else:
        print("Список пуст")
    return lst
list = [1,2,3]
list = remove_last(list)
print(list)
#4
def print_list(lst):
    for i in lst:
        print(i, end=" ")
    print()
list = [1,2,3]
print_list(list)
#5
def find_element(lst):
    a = input()
    if a.isdigit():
        a = int(a)
    if a in lst:
        print("Элемент найден")
    else:
        print("Элемент не найден")
list = [1,2,3]
find_element(list)
#6
def insert_at_position(lst):
    a = input()
    if a.isdigit():
        a = int(a)
    ind = int(input())
    if 0 <= ind <= len(lst):
        lst.insert(ind, a)
    else:
        print("Неверная позиция")
    return lst
list = [1, 2, 3]
list = insert_at_position(list)
print(list)
#7
def remove_by_value(lst):
    a = input()
    if a.isdigit():
        a = int(a)
    if a in lst:
        lst.remove(a)
    else:
        print("Элемент не найден")
    return lst
list = [1, 2, 3]
list = remove_by_value(list)
print(list)
#8
def merge_lists(lst1, lst2):
    return lst1 + lst2
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = merge_lists(list1, list2)
print(result)
#9
def reverse_list(lst):
    lst.reverse()
    return lst
list = [1, 2, 3, 4]
list = reverse_list(list)
print(list)
#10
def sort_list(lst):
    lst.sort()
    return lst
list = [4, 2, 5, 1, 3]
list = sort_list(list)
print(list)
