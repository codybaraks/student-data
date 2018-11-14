from math import pow,pi,sqrt
import datetime
def add(x,y):
    result = x + y
    print(result)

#volume cylinder
#area equi triangle
#name -> saves it in a text file
#three numbers det the largest
#print the current date

add(5,8)
add(8888,8888)

# vol of cylinder
def vol(h,r,pi):
    vol =h *r **2 *pi
    print(vol)


vol(12,4,pi)

def equi(a):
    result = sqrt(3)/2 * pow(a, 2)
    print(result)



side = int(input("Enter Side "))
equi(side)


def numbers(x,y,z):
    if x < y < z:
        print("{} is larger than {} and {}".format(z,y,x))
    if z < y > x:
        print("{} is larger than {} and {}".format(y, x, z))
    elif y > x > z:
        print("{} is larger than {} and {}".format(y, x, z))
    else:
        print("{} is larger than {} and {}".format(x,z,y))


numbers(12,90,10)



now = datetime.datetime.now()
print(now)
