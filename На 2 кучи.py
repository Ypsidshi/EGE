def а(a, b, c, m):
    if a+b>= 41: return c%2 == m%2
    if c == m: return 0
    h = [f(a+1, b, c+1, m),]