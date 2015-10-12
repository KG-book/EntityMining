# -*- coding: utf-8 -*-

import numpy


def hamm_dist(s1, s2):
    u1 = s1.decode('utf8')
    u2 = s2.decode('utf8')
    length = min(len(u1), len(u2))
    dist = 0
    for i in xrange(length):
        if u1[i] != u2[i]:
            dist += 1
    return dist + max(len(u1), len(u2)) - length



def edit_dist(x, y):
    '''计算两个
       [Parameters]
           x/y： unicode编码的两个字符串
       [Return]
           <int>: 两个输入字符串的编辑距离
    '''
    lenx = len(x)
    leny = len(y)
    #recMatrix用来存放已经解过的子问题
    recMatrix = numpy.zeros((lenx+1, leny+1), dtype=int)
    
    #记录边界条件
    recMatrix[:, 0] = range(lenx+1)
    recMatrix[0, :] = range(leny+1)
     
    for m in xrange(lenx):
        for n in xrange(leny):
            #cmpList用来存放候选的子问题推导式
            cmpList = [recMatrix[m, n+1] + 1, recMatrix[m+1, n] + 1]
            if m >= 1 and n >= 1 and x[m-1] == y[n] and x[m] == y[n-1] :
                cmpList.append(recMatrix[m-1, n-1] + 1)
            if x[m] == y[n]:
                cmpList.append(recMatrix[m, n])
            else:
                cmpList.append(recMatrix[m, n]+1)
            #从候选集中选出最优值
            recMatrix[m+1, n+1] = min(cmpList)
    return recMatrix[lenx, leny]      
