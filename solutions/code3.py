####### Solution 3 ######


x = 1
y = 12
a = 1
b = 1


def calculateValue(x,y,a,b):
    
    return x**(a+b)/y**(a+b)
    

if x == 0 and y == 0:
    print("x and y can not be 0")
else:
    print(calculateValue(x,y,a,b))