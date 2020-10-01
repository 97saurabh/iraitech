# solution 1
def sum(n,x):
    
    total = 0
    
    for i in range(1, n+1):
        total = total + (1 / x)**i
    return total
x = 2
n = 5
print(round(sum(x, n),2))


def solutionRec(n,x):
    
    if n == 1:
        return 1/x
    
    else:
        return (1/x)**n + solutionRec(n-1,x)
        
print(round(solutionRec(x, n),2))