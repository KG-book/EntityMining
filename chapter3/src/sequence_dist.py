# -*- coding: utf-8 -*-

def lcs_len(x, y):
    '''计算两个序列的最长公共子序列(Longgest Common Sequence)长度
    [Parameters]
        x/y： 用list, numpy arry, string 或unicode表示的两个序列
    [Return]
       <int>: 两个输入序列的最长公共子序列长度
    '''
    lenx = len(x)
    leny = len(y)
    recMatrix = np.zeros((lenx+1, leny+1), dtype=int)

    for m in xrange(lenx):
        for n in xrange(leny):
            if x[m] == y[n]:
                recMatrix[m+1, n+1] = recMatrix[m, n] + 1
            else:
                recMatrix[m+1, n+1] = max(recMatrix[m, n+1],
					 recMatrix[m+1, n])
    return recMatrix[lenx, leny]
