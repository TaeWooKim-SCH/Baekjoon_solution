# 10-1: 재귀적인 최대공약수
def iGcd(m, n):
    while n > 0:
        m, n = n, m % n
    return m

def rGcd(m, n):
    if m % n == 0:
        return n
    else:
        gcd = rGcd(n, m % n)
        return gcd


# 10-2: 재귀적인 피보나치 수열
def rFib(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        y = rFib(x - 1) + rFib(x - 2)
    return(y)

def iFib(x):
    if x < 2:
        return x
    else:
        f, g = 0, 1
        for i in range(x - 1):
            f, g = g, f + g
        return g


# 10-3: 재귀적인 N-퀸
def noConflicts(borad, current):
    for i in range(current):
        if (borad[i] == borad[current]):
            return False
        if (current - i == abs(borad[current])):
            return False
    return True

def rQueens(board, current, size):
    if (current == size):
        return True
    else: 
        for i in range(size):
            borad[current] = i
            if noConflicts(board, current):
                found = rQueens(borad, current + 1, size)
                if found:
                    return True
        return False