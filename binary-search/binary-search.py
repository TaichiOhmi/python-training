import random
import time

# naive
# リストの全てを確認
# ターゲットがリストにあれば、インデックスを返し、なければ−1を返す。
def naive_search(lis, target):
    # example list = [1, 5, 7, 18]
    for i in range(len(lis)):
        if lis[i] == target:
            return i
    return -1


# リストの最大値と最小値の中間点を取ることを繰り返し、効率よくターゲット値を求める。
def binary_search(lis, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(lis) - 1

    if high < low:
        return -1

    #example lis = [1, 5, 7, 19, 50] # should return 3
    midpoint = (low + high) // 2 # 2で割った整数部分(中間を取る)

    # 中間点がターゲットなら、そのindex(midpoint)を返す。
    if lis[midpoint] == target:
        return midpoint
    # ターゲットより中間点が大きい場合、highを中間点-1にし、再びこの関数を呼ぶ。
    elif target < lis[midpoint]:
        return binary_search(lis, target, low, midpoint-1)
    # ターベットより中間点が小さい場合、lowを中間点+1にし、再びこの関数を呼ぶ。
    else:
        # target > lis[midpoint]
        return binary_search(lis, target, midpoint+1, high)


if __name__=='__main__':
    length = 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive search time: ", (end - start), "seconds")

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary search time: ", (end - start), "seconds")