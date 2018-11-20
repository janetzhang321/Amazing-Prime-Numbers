def euclid(x, y):
    if (x < 0):
        x = -1*x
    if (y < 0):
        y = -1*y
    if (x % y == 0):
        return y
    else:
        return euclid(y,x%y)


if (__name__=="__main__"):
    x = 50
    y = -10
    print(euclid(x,y))
