#coding=utf-8

def get_bag(wei, pi, con):
    length = len(wei)
    arr = [[0 for row in xrange(con+1)] for clo in xrange(length+1)]
    for i in xrange(1, length+1):
        for j in xrange(0, con+1):
            arr[i][j] = arr[i-1][j]
            if j > wei[i-1]:
                arr[i][j] = max(arr[i][j], arr[i-1][j-wei[i-1]] + pieces[i-1])
    return arr

if __name__ == '__main__':
    c = 11
    weights = [2,3,6,5,4]
    pieces = [6,3,5,4,6]
    b = get_bag(weights, pieces, c)
    print b
    print b[5][11]
