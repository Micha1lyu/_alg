# 方法 1
def power2n(n):
    return 2**n

# 方法 2a：用遞迴
def power2n2a(n):
    if n == 0:
        return 1
    return power2n2a(n-1) + power2n2a(n-1)

# 方法2b：用遞迴
def power2n2b(n):
    if n == 0:
        return 1
    return 2 * power2n2b(n-1)

# 方法 3：用遞迴+查表
lookup = [None] * 10000
lookup[0] = 1

def power2n(n):
    if lookup[n] is not None:
        return lookup[n]
    lookup[n] = power2n(n - 1) + power2n(n - 1)
    return lookup[n] 
