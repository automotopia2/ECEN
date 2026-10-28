import math
alpha0 = 0
alpha1 = 1

R6 = 820
R2 = 10000
R7 = 4000
C5 = 0.000000033
C6 = 0.0000000033
Ct = C5 + C6

omega_n = (2*R6 + R2)/(Ct*(R6 + alpha0*R2)*(R6 + R7 + (1 - alpha0)*R2))
omega_d = (2*R6 + R2)/(Ct*(R6 + R2*(1 - alpha0))*(R6 + R7 + alpha0*R2))

H1 = omega_d/omega_n
H2 = omega_n/omega_d

result1 = 20*math.log(H1, 10)
result2 = 20*math.log(H2, 10)

print(f"Omega N: {omega_n}")
print(f"Omega D: {omega_d}\n")
print(f"H(jomega), alpha = 0: {H1}")
print(f"H(jomega), alpha = 1: {H2}\n")
print(f"H(jomega)|dB, alpha = 0: {result1}")
print(f"H(jomega)|dB, alpha = 1: {result2}")