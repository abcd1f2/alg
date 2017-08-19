#coding=utf-8

"""
dp算法
求数塔的最大路径
"""

def digital_tower(n):
    dp = [[0 for clo in xrange(n+1)] for row in xrange(n+1)]
    for i in xrange(n, 0, -1):
        for j in xrange(1, i+1):
            if i + 1 > n:
                dp[i][j] = arr[i][j]
            else:
                dp[i][j] = arr[i][j] + max(dp[i+1][j+1], dp[i+1][j])
    return dp

"""
打印数塔的最大路径
"""
def print_max_path(l):
    last_index = 0
    max_path = []
    for i in xrange(1, 4+1):
        for j in xrange(1, i+1):
            if i == 1 and j == 1:
                max_path.append(arr[i][j])
                last_index = 1
                break
            else:
                if l[i][last_index] > l[i][last_index+1]:
                    max_path.append(arr[i][last_index])
                    break
                else:
                    last_index += 1
                    max_path.append(arr[i][last_index])
                    break
    print max_path

if __name__ == '__main__':
    arr = [[0 for clo in xrange(10)] for row in xrange(10)]
    arr[1] = [0,9,0,0,0,0,0,0,0,0]
    arr[2] = [0,12,15,0,0,0,0,0,0,0]
    arr[3] = [0,10,6,8,0,0,0,0,0,0]
    arr[4] = [0,2,18,9,5,0,0,0,0,0]

    res = digital_tower(4)
    print res
    print res[1][1]
    print_max_path(res)
