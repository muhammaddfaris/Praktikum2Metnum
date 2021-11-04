
# Iterasi Gauss Seidel

# Definisikan Persamaan yang akan diselesaikan
# Dalam bentuk dominan secara diagonal
# Iterasi Gauss Seidel

# Definisikan Persamaan yang akan diselesaikan
# Dalam bentuk dominan secara diagonal
f1 = lambda x,y,z: (-4+3*y-0*z)/4
f2 = lambda x,y,z: (40-2*x+5*z)/-4
f3 = lambda x,y,z: (14+0*x+2*y)/6

# Inisial awal
x0 = 2
y0 = -8
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