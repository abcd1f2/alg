#coding=utf-8

"""
已知有1,2,5,9,10 这几种银币
求总数30最少几个银币
"""
def min_coin(n):
    if n < len(base_arr):
        return base_arr[n]

    min_num = n
    for i in xrange(1,n+1):
        if i < len(base_arr):
            min_num = min(min_num, base_arr[i] + min_coin(n - i))
        else:
            base_arr.append(min_coin(i))
    return min_num

if __name__ == '__main__':
    base_arr = [0,1,1,2,2,1,2,2,3,1,1]
    print min_coin(15)
