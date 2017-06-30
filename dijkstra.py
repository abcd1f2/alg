#coding=utf-8

"""
@parameter
    doub_list: total array
    vertexs:
    edges:
@reutrn
    results
"""
def dijkstra(doub_list, vertexs, edges):
    dist = list()
    book = list()
    for item in doub_list[1]:
        dist.append(item)

    book = [0 for i in xrange(vertexs + 1)]
    book[1] = 1

    u = 1

    #计算所有中间顶点
    for i in xrange(1, vertexs):
        v_min = min_value

        #将未纳入的顶点纳入到计算集合中
        for j in xrange(1, vertexs + 1):
            if book[j] == 0 and dist[j] < v_min:
                v_min = dist[j]
                u = j
        book[u] = 1

        '''
        优化点：将边的权重加入到一个堆中，然后从堆中取最小的值
        '''
        #将刚纳入的顶点进行计算，围绕顶点计算周围的最近顶点
        for v in xrange(1, vertexs + 1):
            if doub_list[u][v] < min_value and dist[v] > dist[u] + doub_list[u][v]:
                dist[v] = dist[u] + doub_list[u][v]
    return dist

if __name__ == "__main__":
    min_value = 999999999
    ll = [
    [min_value,min_value,min_value,min_value,min_value,min_value,min_value],
    [min_value,0,1,12,min_value, min_value, min_value],
    [min_value,min_value,0,9,3,min_value,min_value],
    [min_value,min_value,min_value,0,min_value,5,min_value],
    [min_value,min_value,min_value,4,0,13,15],
    [min_value,min_value,min_value,min_value,min_value,0,4],
    [min_value,min_value,min_value,min_value,min_value,min_value,0]]
    print dijkstra(ll, 6, 9)
