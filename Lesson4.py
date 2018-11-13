#calculate volume of a cylinder with radius 17, height = 80
#calulate area of a sphere with radius 10
#area of equilateral triangle with side 15

# Volume of a cylinder (vol = π r^2 h)

from math import pi,sqrt,pow

radius = 17
height = 80

volume = pi * radius**2 * height

print(volume)

# Area for Sphere (4 π r2)

sphere_radius = 10

Area = 4* pi * pow(sphere_radius,2)

print(Area)

# Area of a equilateral Triangle (sqrt(3)/4  *a^2)

side = 15

Area = sqrt(3)/4 *pow(15,2)
print(Area)

