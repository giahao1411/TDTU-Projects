import sympy as sp

H = lambda t: (t + 1)**(1/2) + 5*t**(1/3)

print("Tree's height when t = 0: ", H(0), "ft")
print("Tree's height when t = 4: ", H(4), "ft")
print("Tree's height when t = 8: ", H(8), "ft")

#b
t = sp.symbols('t')

H_avg = ((t + 1)**(1/2) + 5*t**(1/3))

H_in = sp.integrate(H_avg, (t, 0, 8))
print("Tree's average height for t from 0 to 8 = ", 1/8*H_in.evalf(), "ft")