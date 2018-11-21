def euclid(x,y):
    print("finding the gcd(",x,",",y,")...")
    if (x < 0):
        print(x,"is negative")
        x = -1*x
        print("we multiply",-1*x,"by -1 to get",x)
    if (y < 0):
        print(y,"is negative")
        y = -1*y
        print("we multiply",-1*y,"by -1 to get",y)

    print(x,"mod",y, "=", x%y)
        
    if (x % y == 0):
        print("\nthe gcd is",y)
        
    else:
        euclid(y,x%y)

def test_euclid():
    x = input("enter first number: ")
    y = input("enter second number: ")
    euclid(int(x),int(y))
        
if (__name__=="__main__"):
    #test_euclid()
    
