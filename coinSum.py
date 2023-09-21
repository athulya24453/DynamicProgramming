def f(x, l) -> int:
    if x < 0:
        return float('inf')
    
    if x == 0:
        return 0
    
    best = float('inf')

    for e in l:
        best = min(best ,f((x-e),l)+1)

    return best

l = [1,3,4]
print(f(10, l))