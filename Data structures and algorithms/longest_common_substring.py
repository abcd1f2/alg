#coding=utf-8

"""
dp 算法
"""
def common_substring_dp(s1, s2):
    ls1 = len(s1)
    ls2 = len(s2)
    dis = [[0 for i in xrange(ls2)] for j in xrange(ls1)]
    print dis
    max_len = 0
    for i in xrange(ls1):
        for j in xrange(ls2):
            if s1[i] == s2[j]:
                if i > 0 and j > 0:
                    print i,j
                    dis[i][j] = dis[i-1][j-1] + 1
                else:
                    dis[i][j] = 1

                if dis[i][j] > max_len:
                    max_len = dis[i][j]
    return max_len

"""
暴力搜索
"""
def common_max_length(s1, s2):
    min_l = min(len(s1), len(s2))
    max_l = 0
    for i in xrange(min_l):
        if s1[i] == s2[i]:
            max_l += 1
        else:
            break
    return max_l

def common_substring_base(s1, s2):
    max_len = 0
    for i in xrange(len(s1)):
        for j in xrange(len(s2)):
            tmp_max = common_max_length(s1[i:], s2[j:])
            if tmp_max > max_len:
                max_len = tmp_max
    return max_len


if __name__ == '__main__':
    str1 = 'efgabcd'
    str2 = 'abdef'
    print common_substring_dp(str1, str2)
    print common_substring_base(str1, str2)
