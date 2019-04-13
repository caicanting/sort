# 排序算法的稳定性:若待排序的序列中，经过排序， 这些记录的相对次序保持不变，则称该算法是稳定的；
#               若经排序后，记录的相对次序发生了改变，则称该算法是不稳定的。
# 稳定性的好处：1.排序算法如果是稳定的，那么从一个键上排序，然后再从另一个键上排序，第一个键排序的结果可以为第二个键排序所用。
#            2.基数排序就是这样，先按低位排序，逐次按高位排序，低位相同的元素其顺序再高位也相同时是不会改变的。
#            3.另外，如果排序算法稳定，可以避免多余的比较。
# 稳定的排序算法：冒泡排序、插入排序、归并排序和基数排序
# 不稳定的排序算法：选择排序、快速排序、希尔排序、堆排序


# 如何选择排序算法，是否时间复杂度低的算法就是合适的？
# 影响排序的因素有很多，平均时间复杂度低的算法并不一定就是最优的。相反，有时平均时间复杂度高的算法可能更适合某些特殊情况。


# 排序算法选择的情况（设待排序元素的个数为n）
# 1.当n较大，则应采用时间复杂度为O(nlog2 n)的排序方法：快速排序、堆排序或归并排序。
#          a.快速排序：是目前基于比较的内部排序中被认为是最好的方法，当待排序的关键字是随机分布时，快速排序的平均时间最短。
#          b.堆排序：如果内存空间允许且要求稳定性的。
#          c.归并排序：它有一定数量的数据移动，所以我们可能过与插入排序组合，先获得一定长度的序列，然后再合并，在效率上将有所提高。
# 2.当n较大，内存空间允许，且要求稳定性 =》归并排序
# 3.当n较小，可采用直接插入或直接选择排序。
#          a.直接插入排序：当元素分布有序，直接插入排序将大大减少比较次数和移动记录的次数。
#          b.直接选择排序：元素分布有序，如果不要求稳定性，选择直接选择排序。
# 4.一般不使用或不直接使用冒泡排序
# 5.基数排序
#       它是一种稳定的排序算法，但有一定的局限性：
# 　　   a.关键字可分解。
# 　　   b.记录的关键字位数较少，如果密集更好。
# 　　   c.如果是数字时，最好是无符号的，否则将增加相应的映射复杂度，可先将其正负分开排序。


# 冒泡排序，O(n平方)
def bubble_sort(num):
    for i in range(len(num) - 1):
        for j in range(len(num) - i - 1):
            if num[j] > num[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j]
    return num


# 选择排序，O(n平方)
def selection_sort(num):
    for i in range(len(num) - 1):
        n = num[i]
        index = i
        for j in range(i + 1, len(num)):
            if num[j] < n:
                index = j
                n = num[j]
        num[i], num[index] = num[index], num[i]
    return num


# 插入排序，O(n平方)
def insertion_sort(num):
    for i in range(1, len(num)):
        for j in range(i):
            if num[i] < num[j]:
                num.insert(j, num[i])
                del num[i + 1]
                break
    return num


# 快速排序，平均是O(nlog2 n)，最坏是O(n平方)，思想：冒泡，二分，递归分治
def partition(num, left, right):    # 一次快速排序
    while left < right:
        while num[right] > num[left]:
            right = right - 1
        num[left], num[right] = num[right], num[left]
        while num[left] < num[right]:
            left = left + 1
        num[left], num[right] = num[right], num[left]
    return left


def quick_sort(num, left, right):
    if left >= right:
        return
    middle = partition(num, left, right)
    quick_sort(num, left, middle - 1)
    quick_sort(num, middle + 1, right)
    return num


# 堆排序，O(nlog2 n)，就是完全二叉树
def heap_adjust(num, i, l):     # 调整堆
    while 2 * i + 1 < l:
        left = 2 * i + 1
        right = left + 1
        if left < l - 1 and num[left] < num[right]:
            left = right
        if num[i] < num[left]:
            num[i], num[left] = num[left], num[i]
        else:
            break
        i = left


def heap_sort(num):
    len1 = len(num) - 1
    for i in range(int(len(num) / 2 - 1), -1, -1):  # 只需要考虑0到len(num) / 2 - 1的结点，因为只有这几个结点是根结点
        heap_adjust(num, i, len(num))
    while len1 >= 0:
        num[0], num[len1] = num[len1], num[0]
        heap_adjust(num, 0, len1)
        len1 = len1 - 1
    return num


# 希尔排序，是插入排序的一种体现，也叫缩小增量排序，平均复杂度是O(n的1.3次方)，
def shell_sort(num):
    n = len(num)
    gap = n // 2  # 对半分
    while gap >= 1:
        for j in range(gap, n):
            i = j
            while (i - gap) >= 0:
                if num[i] < num[i - gap]:  # 比较大小，小的放前面，大的放后面
                    num[i], num[i - gap] = num[i - gap], num[i]
                    i = i - gap
                else:
                    break
        gap = gap // 2
    return num


# 归并排序，递归分治思想，O(nlog2 n)
def merge_sort(num):
    if len(num) <= 1:
        return num
    mid = len(num) // 2  # 将列表分成更小的两个列表
    # 分别对左右两个列表进行处理，分别返回两个排序好的列表
    left = merge_sort(num[:mid])
    right = merge_sort(num[mid:])
    # 对排序好的两个列表合并，产生一个新的排序好的列表
    return merge(left, right)


def merge(left, right):
    result = []  # 新的已排序好的列表
    i = 0  # 下标
    j = 0
    # 对两个列表中的元素 两两对比。
    # 将最小的元素，放到result中，并对当前列表下标加1
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


# 计数排序，是桶排序的一种特殊情况，每个桶只放相同的数据
def count_sort(num):
    mmax = int(max(num))
    num1 = [0 for i in range(mmax + 1)]
    for i in range(len(num)):
        num1[int(num[i])] = num1[int(num[i])] + 1
    index = 0
    for i in range(mmax + 1):
        for j in range(num1[i]):
            num[index] = i
            index = index + 1
    return num


# 桶排序，先分配好桶，再对每个非空的桶，进行稳定的其他排序算法，或者再对每个非空的桶进行桶排序
# 桶排序代码，具体分多少个桶，得根据情况设置，代码跟着改
def bucket_sort(num):
    bucket_num = int(max(num) / 10) + 1
    bucket = [[0] for i in range(bucket_num)]
    result = []
    for i in range(len(num)):
        if len(str(num[i])) > 1:
            bucket[int(str(num[i])[0])].append(num[i])
        else:
            bucket[0].append(num[i])
    for i in range(len(bucket)):
        bucket[i][1:] = insertion_sort(bucket[i][1:])
    for i in range(len(bucket)):
        for j in range(1, len(bucket[i])):
            result.append(bucket[i][j])
    return result


# 基数排序，O(d(r+n))其中r代表关键字基数，d代表长度，n代表关键字个数。基数排序，有两种LSD和MSD，分别从低位开始排和从高位开始排。
def radix_sort(num):
    mmax = max(num)
    mmax = len(str(mmax))
    num1 = [['0'] for i in range(10)]
    num = [str(num[i]) for i in range(len(num))]
    p = -1
    while mmax != 0:
        for i in range(len(num)):
            if len(num[i]) >= abs(p):
                index = int(num[i][p])
                num1[index].append(num[i])
            else:
                num1[0].append(num[i])
        num.clear()
        for j in range(10):
            if len(num1[j]) > 1:
                for k in range(1, len(num1[j])):
                    num.append(num1[j][k])
        num1.clear()
        num1 = [['0'] for i in range(10)]
        mmax = mmax - 1
        p = p - 1
    num = [int(num[i]) for i in range(len(num))]
    return num


def main():
    while True:
        try:
            print('请输入待排序的序列，每个数用空格隔开')
            num = input().split()
            if num == '':
                break
            print('1:冒泡排序 2：选择排序 3：插入排序 4：快速排序 5：堆排序 6：希尔排序 7：归并排序 8：计数排序 9：桶排序 10：基数排序')
            choose = int(input())
            num = [int(num[i]) for i in range(len(num))]
            if choose == 1:
                print(bubble_sort(num))
            elif choose == 2:
                print(selection_sort(num))
            elif choose == 3:
                print(insertion_sort(num))
            elif choose == 4:
                right = len(num) - 1
                left = 0
                print(quick_sort(num, left, right))
            elif choose == 5:
                print(heap_sort(num))
            elif choose == 6:
                print(shell_sort(num))
            elif choose == 7:
                print(merge_sort(num))
            elif choose == 8:
                print(count_sort(num))
            elif choose == 9:
                print(bucket_sort(num))
            elif choose == 10:
                print(radix_sort(num))
        except:
            break


if __name__ == '__main__':
    main()