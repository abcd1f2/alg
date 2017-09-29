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

def ViterbiCompute(obs, states, start_p, trans_p, emit_p):
    """
    obs:观测序列
    states:隐状态
    start_p:初始概率(隐状态)
    trans_p:转移概率(隐状态)
    emit_p:发射状态(隐状态表现为显状态的概率)
    return:返回最可能的概率
    """
    v = [[0 for i in xrange(len(states))] for j in xrange(len(obs))]
    path = [[0 for i in xrange(len(obs))] for j in xrange(len(states))]
    for i in states:
        v[0][i] = start_p[i] * emit_p[i][obs[0]]
        path[i][0] = i
    for i in xrange(1, len(obs)):
        newpath = [[0 for j in xrange(len(obs))] for jj in xrange(len(states))]
        for s in states:
            prob = -1
            state = None
            for ss in states:
                tmpprob = v[i-1][ss] * trans_p[ss][s] * emit_p[s][obs[i]]
                if tmpprob > prob:
                    prob = tmpprob
                    state = ss
                    v[i][s] = prob
                    for m in xrange(i):
                        newpath[s][m] = path[state][m]
                    newpath[s][i] = s
        path = newpath
    prob = -1
    state = 0
    for y in states:
        if v[len(obs)-1][y] > prob:
            prob = v[len(obs)-1][y]
            state = y
    return path[state]

def ViterbiComputePy(obs, states, start_p, trans_p, emit_p):
    """
    obs:观测序列
    states:隐状态
    start_p:初始概率(隐状态)
    trans_p:转移概率(隐状态)
    emit_p:发射状态(隐状态表现为显状态的概率)
    return:返回最可能的概率
    """
    v=[{}] #[时间][隐状态]=概率
    path={} #中间变量代表当前状态是哪个隐状态
    #初始状态 t=0
    for i in states:
        v[0][i] = start_p[i] * emit_p[i][obs[0]]
        path[i] = [i]
    #t>0执行一遍viterbi
    for t in xrange(1, len(obs)):
        v.append({})
        newpath = {}
        for k in states:
            #概率 隐状态 = 昨天的概率 * 转换概率 * 活动概率
            prob,state = max((v[t-1][m]*trans_p[m][k]*emit_p[k][obs[t]],m) for m in states)
            v[t][k] = prob
            newpath[k] = path[state] + [k]
        path = newpath
    prob,state = max((v[len(obs)-1][m],m) for m in states)
    return prob,path[state]

if __name__ == '__main__':
    s = [0,1]
    o = [0,1,2]
    s_p = [0.6,0.4]
    t_p = [[0.7,0.3],[0.6,0.4]]
    e_p = [[0.1,0.4,0.5],[0.6,0.3,0.1]]
    print ViterbiCompute(o, s, s_p, t_p, e_p)
    print ViterbiComputePy(o, s, s_p, t_p, e_p)

    import sys
    sys.exit(0)
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
