#coding=utf-8

def edit_distance(s1, s2):
    ls1 = len(s1)
    ls2 = len(s2)
    if ls1 <= 0 or ls2 <= 0:
        return max(ls1, ls2)

    arr = [[0 for clo in xrange(ls2+1)] for row in xrange(ls1+1)]
    for i in xrange(ls1+1):
        arr[i][0] = i
    for j in xrange(ls2+1):
        arr[0][j] = j
    for i in xrange(1,ls1+1):
        for j in xrange(1,ls2+1):
            if s1[i-1] == s2[j-1]:
                arr[i][j] = min(arr[i-1][j-1], arr[i][j-1]+1,arr[i-1][j]+1)
            else:
                arr[i][j] = min(arr[i-1][j-1]+1, arr[i-1][j]+1,arr[i][j-1]+1)
    return arr[i][j]


if __name__ == '__main__':
    s1 = 'hello'
    s2 = 'helloee'
    ell = edit_distance(s1, s2)
    print '相似性为 {0}'.format(1-float(ell)/max(len(s1),len(s2)))
