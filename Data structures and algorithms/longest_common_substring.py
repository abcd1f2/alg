#coding=utf-8

def common_substring(s1, s2):
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

if __name__ == '__main__':
    str1 = 'efgabcd'
    str2 = 'abcdef'
    print common_substring(str1, str2)
