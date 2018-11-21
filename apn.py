import math
import random

#1 EUCLID'S ALGORITHM
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
        return y
    else:
        return euclid(y,x%y)

def test_euclid():
    x = input("enter first number: ")
    y = input("enter second number: ")
    euclid(int(x),int(y))

#2 GENERATING PRIME NUMBERS
def print_list(L):
    s=""
    for x in L:
        s += str(x)+","
        print("["+s[0:-1]+"]")


def sieve_gen(n):
    n+=1
    A = [True for i in range(n)]
    for i in range(2,int(math.sqrt(n))+1):
        j = 0
        B = []
        while(i**2+j*i < n):
            B.append(i**2+j*i)
            j+=1
        for x in B:
            A[x] = False
            P = []
            a = 2
    while a < n:
        if A[a]:
            P.append(a)
            a+=1
    return P

def test_sieve():
    n = input("enter a number: ")
    print_list(sieve_gen(int(n)))

#3 PRIMALITY TEST
def trial_division(n):
    print("checking for a prime number between 2 and sqrt(",n,") that divides", n)
    print("checking",sieve_gen(int(math.sqrt(n))));
    for x in sieve_gen(int(math.sqrt(n))):
        if n%x == 0:
            print(n, "is not prime it is divisible by",x)
            return False
        print(n, "is prime")
    return True

def sieve_primality(n):
    print("generating prime numbers using Sieve of Eratosthenes")
    print_list(sieve_gen(n))
    if (n<4):
        print(n, "is prime")
        return True
    elif (sieve_gen(n)[-1] == n):
        print(n,"is prime because it is in the list") 
        return True
    else:
        print(n,"is not prime because it is not in the list")
        return False

def fermat_little_theorem(n):
    if n<4:
        print(n,"is prime")
        return True
    else:
        
        a = random.randint(2,n-2)
        print("picking a random number",a,"to test with")
        if n%a==0:
            print(n, "is not prime, it is divisible by", a)
            return False
        else:
            print("testing if (",a,"^ (",n,"- 1 ) %",n,") == 0")
            if ((a**(n-1) - 1)%n == 0):
                print(n, "is prime")
                return False
            else:
                print(n, "is not prime")
                return True

def test_primality():
    print("Tests for Primality:")
    print("1: Trial Division")
    print("2: Sieve of Eratosthenes")
    print("3: Fermat Little Theroem")
    test = input("pick a test: ")
    if int(test) > 0 and int(test) < 4:
        n = input("enter a number to test: ")
        if int(test) == 1:
            trial_division(int(n))
        elif int(test) == 2:
            sieve_primality(int(n))
        elif int(test) == 3:
            fermat_little_theorem(int(n))
            
    else:
        test_primality()
        
    
if (__name__=="__main__"):
    #test_euclid()
    #test_sieve()
    test_primality()
