#coding=utf-8

'''
@parameter
    ll: arrary
    st: start search
'''
def bfs(ll, st):
    tmp = [st,]
    flags = [0 for i in xrange(len(ll) + 1)]
    flags[st] = 1
    while len(tmp) > 0:
        i = tmp[0]
        tmp.pop(0)
        print i
        for j in xrange(1, len(ll) + 1):
            if flags[j] <= 0 and ll[i-1][j-1] > 0:
                tmp.append(j)
                flags[j] = 1

if __name__ == '__main__':
    double_list = [[0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0]]
    for i in xrange(1, len(double_list) + 1):
        print "i ", i
        bfs(double_list, i)
