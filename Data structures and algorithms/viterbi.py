#coding=utf-8

"""
参考：http://www.jianshu.com/p/218c1e4f0891
计算从A到B的最短路径
将同一列定位一个点
"""
def viterbi():
    for i in xrange(1,10):
        k = x
        for j in xrange(i):
            if data[j][i] < x and dist[j] + data[j][i] < k:
                k = dist[j] + data[j][i]
                print j,i,dist[j]
        dist[i] = k

if __name__ == '__main__':
    x = 99999999
    data = [[x,4,2,3,x,x,x,x,x,x],
            [x,x,x,x,10,9,x,x,x,x],
            [x,x,x,x,6,7,10,x,x,x],
            [x,x,x,x,x,3,8,x,x,x],
            [x,x,x,x,x,x,x,4,8,x],
            [x,x,x,x,x,x,x,9,6,x],
            [x,x,x,x,x,x,x,5,4,x],
            [x,x,x,x,x,x,x,x,x,8],
            [x,x,x,x,x,x,x,x,x,4],
            [x,x,x,x,x,x,x,x,x,x]]
    dist = [0 for i in xrange(10)]
    viterbi()
    print dist
