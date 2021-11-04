# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 06:02:36 2021

@author: Muhammad Faris
"""

# Iterasi Gauss Seidel

# Definisikan Persamaan yang akan diselesaikan
# Dalam bentuk dominan secara diagonal
f1 = lambda x,y,z: (7.85+0.1*y+0.2*z)/3
f2 = lambda x,y,z: (-19.3-0.1*x+0.3*z)/7
f3 = lambda x,y,z: (71.4-0.3*x+0.2*y)/10

# Inisial awal
x0 = 1
y0 = 2
z0 = 2
step = 1

# Input nilai galat/error
e = float(input('Input Toleransi error: '))

# Implementasi iterasi Gauss Seidel
print('\nStep\tx\ty\tz\n')

condition = True

while condition:
    x1 = f1(x0,y0,z0)
    y1 = f2(x1,y0,z0)
    z1 = f3(x1,y1,z0)
    print('%d\t%0.4f\t%0.4f\t%0.4f\n' %(step, x1,y1,z1))
    e1 = abs(x0-x1);
    e2 = abs(y0-y1);
    e3 = abs(z0-z1);

    step +=1
    x0 = x1
    y0 = y1
    z0 = z1

    condition = e1>e and e2>e and e3>e
print('\nSolusi: x=%0.3f, y=%0.3f and z = %0.3f\n'% (x1,y1,z1))